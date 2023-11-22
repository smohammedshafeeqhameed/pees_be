from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import CustomUser

class SleepLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    day_of_week = models.CharField(max_length=20, blank=True)
    bedtime = models.TimeField(null=True, blank=True)
    wake_up_time = models.TimeField(null=True, blank=True)
    total_sleep_duration = models.DecimalField(max_digits=4, decimal_places=2, default=0)  # In hours
    naps_duration_hour = models.IntegerField(default=0)
    naps_duration_minutes = models.IntegerField(default=0)
    sleep_environment = models.TextField(blank=True)
    pre_sleep_routine = models.TextField(blank=True)
    quality_of_sleep = models.PositiveIntegerField(default=0)
    naps = models.IntegerField(default=0)
    sleep_disturbances = models.TextField(blank=True)
    dreams_or_nightmares = models.TextField(blank=True)
    feeling_upon_waking = models.CharField(max_length=50, blank=True)
    difficulty_falling_asleep = models.PositiveIntegerField(
        choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], null=True, blank=True)
    difficulty_staying_asleep = models.PositiveIntegerField(
        choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], null=True, blank=True)
    problems_waking_up_early = models.PositiveIntegerField(
        choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], null=True, blank=True)
    satisfaction_with_sleep = models.PositiveIntegerField(
        choices=[(0, 'Very Satisfied'), (1, 'Satisfied'), (2, 'Moderately Satisfied'), (3, 'Dissatisfied'),
                 (4, 'Very Dissatisfied')], null=True, blank=True)
    noticeable_impairment = models.PositiveIntegerField(
        choices=[(0, 'Not at all Noticeable'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much')], null=True, blank=True)
    worried_distressed = models.PositiveIntegerField(
        choices=[(0, 'Not at all Worried'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much'), (4, 'Very Much Worried')],
        null=True, blank=True)
    interference_with_daily_functioning = models.PositiveIntegerField(
        choices=[(0, 'Not at all Interfering'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much'),
                 (4, 'Very Much Interfering')], null=True, blank=True)
    total_score = models.PositiveIntegerField(null=True, blank=True)  # This will store the calculated total score

    def calculate_total_score(self):
        # Check if each value is not None before adding
        values_to_add = [
            self.difficulty_falling_asleep,
            self.difficulty_staying_asleep,
            self.problems_waking_up_early,
            self.satisfaction_with_sleep,
            self.noticeable_impairment,
            self.worried_distressed,
            self.interference_with_daily_functioning,
        ]

        # Filter out None values and calculate the total score
        valid_values = [value for value in values_to_add if value is not None]
        self.total_score = sum(valid_values)
    def __str__(self):
        return f"Sleep Log - {self.date}"


@receiver(pre_save, sender=SleepLog)
def update_total_score(sender, instance, **kwargs):
    instance.calculate_total_score()

class SensorData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    temperature_file = models.FileField(upload_to='sensor_data/temperature/')
    noise_file = models.FileField(upload_to='sensor_data/noise/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sensor Data - {self.timestamp}"