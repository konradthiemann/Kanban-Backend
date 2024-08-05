from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework.response import Response
from rest_framework.views import APIView
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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        errors = {}
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        email = request.data.get('email')
        
        if not username:
            errors['username'] = ['This field may not be blank.']
        elif User.objects.filter(username=username).exists():
            errors['username'] = ['Username is already taken.']
        
        if not password:
            errors['password'] = ['This field may not be blank.']
        elif len(password) < 8:
            errors['password'] = ['Password must be at least 8 characters long.']
        
        if not first_name:
            errors['first_name'] = ['This field may not be blank.']
        
        if not last_name:
            errors['last_name'] = ['This field may not be blank.']
        
        if not email:
            errors['email'] = ['This field may not be blank.']
        elif '@' not in email:
            errors['email'] = ['Invalid email address.']
        elif User.objects.filter(email=email).exists():
            errors['email'] = ['Email is already taken.']

        if not confirm_password:
            errors['confirm_password'] = ['This field may not be blank.']
        elif password != confirm_password:
            errors['confirm_password'] = ['Passwords do not match.']
        
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)