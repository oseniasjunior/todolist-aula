from rest_framework import viewsets
from core import serializers, models


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all() # select * from tasks
    serializer_class = serializers.TaskSerializer
    #
    # # POST
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
    #
    # # PUT
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # # PATCH
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
    #
    # # GET by ID /${id}
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    #
    # # GET
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    #
    # # DELETE
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

