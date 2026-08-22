from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    created_on = filters.DateFromToRangeFilter(
        field_name = 'created_on',
    )

    class Meta:
        model = Task
        fields = []
