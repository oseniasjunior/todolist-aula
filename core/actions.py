from django.utils.timezone import localtime

from core import models


class TaskWorkTimeActions:
    @staticmethod
    def calculate_total_work_hours(task_work_time: 'models.TaskWorkTime'):
        task = task_work_time.task
        task.total_worked_hours += task_work_time.hours
        task.save()


class TaskActions:
    @staticmethod
    def generate_report_task():
        _localtime = localtime()
        tasks - models.Task.objects.all()
        with open(f'report{-_localtime}.txt', 'w') as file:
            for task in tasks:
                file.write(f'{task.title} - {task.total_worked_hours}\n')
