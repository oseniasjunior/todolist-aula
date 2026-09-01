from django.db import models
from core import models as core_models


class TaskQuerySet(models.QuerySet):
    def is_done(self):
        return self.filter(status=core_models.Task.Status.DONE)


class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)

    def is_done(self):
        return self.get_queryset().is_done()
