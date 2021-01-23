from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://niits:abcd1234@localhost/page'
# SQLALCHEMY_ECHO = True
CELERY_BROKER_URL = 'sqla+postgresql://niits:abcd1234@localhost/page'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'example_task': {
        'task': 'tasks.example_task',
        'schedule': timedelta(seconds=10),
        'args': ()
    },
}

ERROR_404_HELP = False
