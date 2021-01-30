from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://niits:abcd1234@db:5432/page'
# SQLALCHEMY_ECHO = True
CELERY_BROKER_URL = 'sqla+postgresql://niits:abcd1234@db:5432/page'
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
