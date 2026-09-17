from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import serializers, models, filters, tasks


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()  # select * from tasks
    serializer_class = serializers.TaskSerializer
    filterset_class = filters.TaskFilter
    ordering_fields = '__all__'
    ordering = ('-id',)

    @action(methods=['post'], detail=True)
    def create_file(self, request, *args, **kwargs):
        task = self.get_object()
        tasks.create_file.delay(task.id)
        # tasks.create_file(task.id)
        return Response(status=status.HTTP_200_OK, data={'message': 'O arquivo está sendo gerado'})

    #
    # @action(methods=['GET'], detail=False)
    # def get_by_name(self, request, *args, **kwargs):
    #     title = request.query_params.get('title', '')
    #     self.queryset = self.queryset.filter(title__icontains=title)
    #     return super().list(request, *args, **kwargs)

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


class TaskWorkTimeModelViewSet(viewsets.ModelViewSet):
    queryset = models.TaskWorkTime.objects.all()
    serializer_class = serializers.TaskWorkTimeSerializer
