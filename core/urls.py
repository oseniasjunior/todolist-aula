from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('tasks', viewsets.TaskModelViewSet)

urlpatterns = router.urls