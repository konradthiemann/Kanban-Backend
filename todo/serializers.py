from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'username',
                  'email'
                  ]

class TodoSerializer(serializers.HyperlinkedModelSerializer):

    # assigned_to = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    #     )
    
    # TODO: Erklärung für author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    author = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ['title',
                #   'created_at',
                #   'description',
                #   'due_date',
                #   'category',
                #   'status',
                #   'urgency',
                #   'assigned_to',
                  'author'
                  ]
