from rest_framework import serializers
from .models import *

class SleepLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepLog
        fields = '__all__'


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('user', 'date', 'temperature_file', 'noise_file', 'timestamp')