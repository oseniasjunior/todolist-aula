from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('tasks', viewsets.TaskModelViewSet)
router.register('tasks_work_time', viewsets.TaskWorkTimeModelViewSet)

urlpatterns = router.urls