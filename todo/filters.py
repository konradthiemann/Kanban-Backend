import django_filters
from .models import Todo, Category
from django.contrib.auth.models import User

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
        model = Category
        fields = ['name']

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains') # icontains: Fallunabhängige Überprüfung, unabhängig von Kein- und Großschreibung
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]
