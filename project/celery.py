import os
from time import sleep
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

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

# using normal schedule
# app.conf.beat_schedule = {
#     'every_25_seconds': {
#         'task': 'celeryPractice.tasks.add1',
#         'schedule': 25,
#         'args': (20, 20),
#     }
# }

# using timedelta
# app.conf.beat_schedule = {
#     'every_25_seconds': {
#         'task': 'celeryPractice.tasks.add1',
#         'schedule': timedelta(seconds=25),
#         'args': (20, 20),
#     }
# }


# using crontab
app.conf.beat_schedule = {
    'every_25_seconds': {
        'task': 'celeryPractice.tasks.add1',
        # 'schedule': crontab(), # every minute
        # 'schedule': crontab(minute='*/1'), # every minute
        # 'schedule': crontab(minute='*/15'), # every 15 minutes
        # 'schedule': crontab(hour='*/1'), # every hour
        # 'schedule': crontab(minute='*/1', hour='*/1'), # every hour
        # 'schedule': crontab(minute=0, hour=0), # every day at 00:00
        'schedule': crontab(minute=0, hour=0, day_of_month=1), # every month at 00:00
        'args': (20, 20),
    }
}

# app.conf.beat_schedule = {
#     'send_email': {
#         'task': 'celeryPractice.tasks.send_email',
#         'schedule': 1,
#     }
# }

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')