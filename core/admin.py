from django.contrib import admin
from core import models


# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'estimated_hours', 'owner')
    search_fields = ('title', 'owner__username')
