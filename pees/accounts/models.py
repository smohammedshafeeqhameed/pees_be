from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
                              null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username