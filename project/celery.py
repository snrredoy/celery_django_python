import os
from time import sleep

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task
def add(x, y):
    sleep(10)
    return x + y

app.conf.beat_schedule = {
    'every_25_seconds': {
        'task': 'celeryPractice.tasks.add1',
        'schedule': 25,
        'args': (20, 20),
    }
}

app.conf.beat_schedule = {
    'send_email': {
        'task': 'celeryPractice.tasks.send_email',
        'schedule': 1,
    }
}

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')