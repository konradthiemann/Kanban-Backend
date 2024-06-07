import django_filters
from .models import Todo

'''
use filter by:
/todos/?title=test
Leerzeichen: '%20'
'''
class TodoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains') # icontains: Fallunabhängige Überprüfung, unabhängig von Kein- und Großschreibung

    class Meta:
        model = Todo
        fields = ['title']
