from django.db import models

class SleepMyth(models.Model):
    myth = models.CharField(max_length=200)
    fact = models.TextField()

    def __str__(self):
        return self.myth
