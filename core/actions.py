from core import models


class TaskWorkTimeActions:
    @staticmethod
    def calculate_total_work_hours(task_work_time: 'models.TaskWorkTime'):
        task = task_work_time.task
        task.total_worked_hours += task_work_time.hours
        task.save()
