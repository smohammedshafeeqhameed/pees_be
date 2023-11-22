# Generated by Django 4.2.5 on 2023-11-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phoneNumber', models.CharField(max_length=20)),
                ('iconName', models.CharField(max_length=50)),
            ],
        ),
    ]