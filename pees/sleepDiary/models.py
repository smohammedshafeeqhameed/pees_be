from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class SleepLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    day_of_week = models.CharField(max_length=20)  # You can use choices for day of the week
    bedtime = models.TimeField()
    wake_up_time = models.TimeField()
    total_sleep_duration = models.DecimalField(max_digits=4, decimal_places=2)  # In hours
    naps = models.TextField(blank=True, null=True)  # Store nap durations as a comma-separated string
    sleep_environment = models.TextField()
    pre_sleep_routine = models.TextField()
    quality_of_sleep = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    sleep_disturbances = models.TextField(blank=True, null=True)
    dreams_or_nightmares = models.TextField(blank=True, null=True)
    feeling_upon_waking = models.CharField(max_length=50)

    def __str__(self):
        return f"Sleep Log - {self.date}"


class SensorData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    temperature_file = models.FileField(upload_to='sensor_data/temperature/')
    noise_file = models.FileField(upload_to='sensor_data/noise/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sensor Data - {self.timestamp}"