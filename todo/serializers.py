from rest_framework import serializers
from .models import Todo, Category
from django.contrib.auth.models import User

# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for the User model.

    This serializer is used to convert User model instances into JSON
    representations and vice versa. It specifies the fields that should
    be included in the serialized output.

    Fields:
        :parameter model (class): The User model class.
        :parameter fields (list): The list of fields to be included in the serialized output.

    """
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
    """
    Serializer for the Todo model.

    Fields:
        :parameter id (int): The ID of the todo.
        :parameter title (str): The title of the todo.
        :parameter description (str): The description of the todo.
        :parameter due_date (int): The due date of the todo.
        :parameter urgency (str): The urgency level of the todo.
        :parameter status (str): The current status of the todo.
        :parameter category (Category): The category of the todo.
        :parameter assigned_to (list): The users assigned to the todo.
        :parameter author (User): The author of the todo.

    """
    author = UserSerializer(
        read_only=True
    )
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
    )
    due_date = serializers.IntegerField(
        required=False,
        allow_null=True
    ) 
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )
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
    """
    Serializer class for the Category model.

    This serializer is used to convert Category model instances into JSON
    representation and vice versa.

    Fields:
        :parameter id (int): The ID of the category.
        :parameter name (str): The name of the category.

    """
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]
