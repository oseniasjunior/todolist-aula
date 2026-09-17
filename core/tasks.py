from celery import shared_task


@shared_task(queue='default')
def create_file(task_id: int):
    with open(f'file_{task_id}.txt', 'w') as file:
        for n in range(1, 10001):
            file.write(f'{n}_{task_id}\n')
