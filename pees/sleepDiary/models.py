from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    difficulty_falling_asleep = models.PositiveIntegerField(
        choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], blank=True, null=True)
    difficulty_staying_asleep = models.PositiveIntegerField(
        choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], blank=True, null=True)
    problems_waking_up_early = models.PositiveIntegerField(
        choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], blank=True, null=True)
    satisfaction_with_sleep = models.PositiveIntegerField(
        choices=[(0, 'Very Satisfied'), (1, 'Satisfied'), (2, 'Moderately Satisfied'), (3, 'Dissatisfied'),
                 (4, 'Very Dissatisfied')], blank=True, null=True)
    noticeable_impairment = models.PositiveIntegerField(
        choices=[(0, 'Not at all Noticeable'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much')], blank=True, null=True)
    worried_distressed = models.PositiveIntegerField(
        choices=[(0, 'Not at all Worried'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much'), (4, 'Very Much Worried')], blank=True, null=True)
    interference_with_daily_functioning = models.PositiveIntegerField(
        choices=[(0, 'Not at all Interfering'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much'),
                 (4, 'Very Much Interfering')], blank=True, null=True)
    total_score = models.PositiveIntegerField(blank=True, null=True)  # This will store the calculated total score

    def calculate_total_score(self):
        self.total_score = (self.difficulty_falling_asleep + self.difficulty_staying_asleep +
                            self.problems_waking_up_early + self.satisfaction_with_sleep +
                            self.noticeable_impairment + self.worried_distressed +
                            self.interference_with_daily_functioning)

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