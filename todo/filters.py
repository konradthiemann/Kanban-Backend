import django_filters
from .models import Todo

'''
use filter by:
/todos/?title=test
Leerzeichen: '%20'
'''
class TodoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Todo
        fields = ['title',
                  'due_date',
                  'urgency',
                  'status',
                  'category',
                  'assigned_to',
                  'description',
                  'author'
        ]

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Todo
        fields = ['name']

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains') # icontains: Fallunabhängige Überprüfung, unabhängig von Kein- und Großschreibung

    class Meta:
        model = Todo
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
