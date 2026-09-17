from django.db.models.signals import post_save
from django.dispatch import receiver
from core import models, actions


@receiver(post_save, sender=models.TaskWorkTime, dispatch_uid='calculate_total_work_hours')
def calculate_total_work_hours(sender, **kwargs):
    task_work_time = kwargs.get('instance')
    actions.TaskWorkTimeActions.calculate_total_work_hours(
        task_work_time=task_work_time
    )
