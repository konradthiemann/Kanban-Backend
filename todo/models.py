from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

# class Urgency(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()

#     def __str__(self) -> str:
#         return self.name


class Todo(models.Model):
    title = models.CharField(max_length=30)
    # urgency = models.CharField(max_length=30)
    # created_at = models.DateField(default=datetime.date.today)
    # description = models.TextField(max_length=500)
    # due_date = models.DateTimeField()
    # assigned_to = models.CharField(max_length=30)
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.CASCADE,
    #     null=True,
    # )
    # status = models.ForeignKey(
    #     Status,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     )
    # urgency = models.ForeignKey(
    #     Urgency,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     )
    # assigned_to = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     default=None,
    #     null=True,
    # )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self) -> str:
        return self.title
