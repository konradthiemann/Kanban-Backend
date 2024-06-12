from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    """
    Represents a category for tasks in the Kanban app.

    Fields:
        name (str): The name of the category.

    Methods:
        __str__(): Returns a string representation of the category.

    """

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Todo(models.Model):
    """
    Represents a task or item on a to-do list.

    Fields:
        :parameter title (str): The title of the todo.
        :parameter description (str): The description of the todo.
        :parameter due_date (datetime): The due date of the todo.
        :parameter urgency (str): The urgency level of the todo.
        :parameter status (str): The status of the todo.
        :parameter Category (Category): The category of the todo.
        :parameter assigned_to (User): The users assigned to the todo.
        :parameter created_at (date): The date the todo was created.
        :parameter author (User): The author of the todo.

    """

    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('review', 'Review'),
        ('done', 'Done'),
    ]

    title = models.CharField(
        max_length=30
    )
    description = models.TextField(
        max_length=500
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True
    )
    urgency = models.CharField(
        max_length=6,
        choices=URGENCY_CHOICES,
        default='medium'
    )
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='todo'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    assigned_to = models.ManyToManyField(
        User,
        related_name='assigned_to',
        blank=True
    )
    created_at = models.DateField(
        default=datetime.date.today
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self) -> str:
        return self.title
