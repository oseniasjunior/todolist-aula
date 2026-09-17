from django_filters import rest_framework as filters
from core import models

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    # start_estimated_hours = filters.NumberFilter(lookup_expr='gte', field_name='estimated_hours')
    # end_estimated_hours = filters.NumberFilter(lookup_expr='lte', field_name='estimated_hours')
    estimated_hours = filters.NumericRangeFilter(lookup_expr='range')

    class Meta:
        model = models.Task
        fields = []