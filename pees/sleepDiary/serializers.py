from rest_framework import serializers
from .models import *


class SleepLogSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = SleepLog
        fields = '__all__'
        extra_fields = ['user_name']


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('user', 'date', 'temperature_file', 'noise_file', 'timestamp')