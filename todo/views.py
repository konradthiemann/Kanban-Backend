from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo, Category
from .serializers import TodoSerializer, CategorySerializer, UserSerializer
from .filters import TodoFilter, CategoryFilter, UserFilter

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

@api_view(['GET'])
def search_tasks(request):
    search_string = request.query_params.get('q', '')
    if search_string:
        tasks = Todo.objects.filter(
            Q(title__icontains=search_string) | 
            Q(description__icontains=search_string) |
            Q(urgency__icontains=search_string) |
            Q(status__icontains=search_string) 
        )
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "A search query is required."}, status=400)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    