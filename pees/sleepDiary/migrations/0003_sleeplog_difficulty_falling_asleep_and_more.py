# Generated by Django 4.2.5 on 2023-10-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleepDiary', '0002_sensordata'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleeplog',
            name='difficulty_falling_asleep',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], null=True),
        ),
        migrations.AddField(
            model_name='sleeplog',
            name='difficulty_staying_asleep',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], null=True),
        ),
        migrations.AddField(
            model_name='sleeplog',
            name='interference_with_daily_functioning',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Not at all Interfering'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much'), (4, 'Very Much Interfering')], null=True),
        ),
        migrations.AddField(
            model_name='sleeplog',
            name='noticeable_impairment',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Not at all Noticeable'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much')], null=True),
        ),
        migrations.AddField(
            model_name='sleeplog',
            name='problems_waking_up_early',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'None'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')], null=True),
        ),
        migrations.AddField(
            model_name='sleeplog',
            name='satisfaction_with_sleep',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Very Satisfied'), (1, 'Satisfied'), (2, 'Moderately Satisfied'), (3, 'Dissatisfied'), (4, 'Very Dissatisfied')], null=True),
        ),
        migrations.AddField(
            model_name='sleeplog',
            name='total_score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sleeplog',
            name='worried_distressed',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Not at all Worried'), (1, 'A Little'), (2, 'Somewhat'), (3, 'Much'), (4, 'Very Much Worried')], null=True),
        ),
    ]
