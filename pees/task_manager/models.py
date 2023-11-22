from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    key = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=20)
    iconName = models.CharField(max_length=50)

    def __str__(self):
        return self.name
