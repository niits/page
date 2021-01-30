import os
import datetime

from celery import Celery
from flask import Flask, render_template, request

from database import migrate, db, Request
from blueprints import main

config_variable_name = 'FLASK_CONFIG_PATH'
default_config_path = os.path.join(os.path.dirname(__file__), 'config/local.py')
os.environ.setdefault(config_variable_name, default_config_path)


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)

    if config_file:
        app.config.from_pyfile(config_file)
    else:
        app.config.from_envvar(config_variable_name)

    if settings_override:
        app.config.update(settings_override)

    init_app(app)

    return app


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    @app.after_request
    def after_request(response):
        r = Request()
        r.ip_address = request.headers['Host']
        r.path = request.path
        r.time = datetime.datetime.now().isoformat()
        r.user_agent = request.headers['User-Agent']
        r.status = response.status_code
        r.method = request.method
        r.size = response.content_length
        r.referrer = request.referrer
        db.session.add(r)
        db.session.commit()
        return response
    @app.route('/')
    def index():
        return render_template('home.html')

    app.register_blueprint(main.bp)


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery