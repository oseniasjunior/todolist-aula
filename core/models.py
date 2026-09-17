from django.db import models
from django.utils.translation import gettext_lazy as _
from core import managers


# Create your models here.
class Task(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = '0', _('Not Started')
        IN_PROGRESS = '1', _('In Progress')
        DONE = '2', _('Done')

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, db_column='tx_title', verbose_name=_('Title'))
    estimated_hours = models.IntegerField(db_column='nb_estimated_hours')
    status = models.CharField(
        max_length=1,
        db_column='cs_status',
        choices=Status.choices,
        default=Status.NOT_STARTED
    )
    owner = models.ForeignKey(
        to='auth.User',
        on_delete=models.DO_NOTHING,
        db_column='id_user'
    )
    total_worked_hours = models.IntegerField(db_column='nb_total_worked_hours', default=0)

    objects = managers.TaskManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        managed = True


class TaskWorkTime(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(
        to='Task',
        on_delete=models.DO_NOTHING,
        db_column='id_task'
    )
    hours = models.IntegerField(db_column='nb_hours')
    date = models.DateTimeField(db_column='dt_date', auto_now_add=True)

    class Meta:
        db_table = 'task_work_time'
        managed = True
