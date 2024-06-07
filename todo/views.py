from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from .models import Todo
from .serializers import TodoSerializer
from .filters import TodoFilter

"""
API endpoint
"""
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        todo = Todo.objects.create(
            title = self.request.POST.get('title', ''),
            author = self.request.user,
        )
        serialized_obj = serializers.serialize('json', [todo])
        return HttpResponse(serialized_obj, content_type='application/json')

            # description = request.POST.get('description', ''),
            # due_date = request.POST.get('due_date', ''),
            # category = request.POST.get('category', ''),
            # status = request.POST.get('status', ''),
            # urgency = request.POST.get('urgency', ''),
            # assigned_to = request.POST.get('assigned_to', ''),
            # assigned_to = request.POST.get('assigned_to', ''),
    # def allow_methods(self):
    #     self.allow_methods = ['GET', 'POST', 'PUT', 'DELETE']
    #     return [method.upper() for method in self.http_method_names if hasattr(self, method)]