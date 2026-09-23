from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anoreg_aula.settings')

app = Celery('anoreg_aula')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('report', Exchange('report'), routing_key='report'),
)

TASKS = {
    'report_tasks': {
        'task': 'core.tasks.report_tasks',
        'schedule': 5
    },
}

app.conf.beat_schedule = TASKS

app.conf.timezone = 'America/Manaus'
app.autodiscover_tasks()
