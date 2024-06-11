from rest_framework import serializers
from .models import Todo, Category
from django.contrib.auth.models import User

# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email'
        ]

class TodoSerializer(serializers.ModelSerializer):
    author = UserSerializer(
        read_only=True
    )
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
    )
    due_date = serializers.IntegerField() 
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'due_date',
            'urgency',
            'status',
            'category',
            'assigned_to',
            'author'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]
