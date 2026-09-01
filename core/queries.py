from core import models

def filter_by_name(name : str = None):
    queryset = models.Task.objects.all()
    if name:
        queryset = queryset.filter(title__icontains=name)
    return queryset

results = filter_by_name()
print(results)