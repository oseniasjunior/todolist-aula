from celery import shared_task
from core import actions

@shared_task(queue='default')
def create_file(task_id: int):
    with open(f'file_{task_id}.txt', 'w') as file:
        for n in range(1, 100000001):
            file.write(f'{n}_{task_id}\n')

@shared_task()
def report_tasks():
    actions.TaskActions.generate_report_task()