from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import generics
from rest_framework.parsers import FileUploadParser


class SleepLogCreate(generics.CreateAPIView):
    queryset = SleepLog.objects.all()
    serializer_class = SleepLogSerializer
    permission_classes = [IsAuthenticated]


class SleepLogList(generics.ListAPIView):
    serializer_class = SleepLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return SleepLog.objects.filter(user=user)


class SensorDataCreateView(generics.CreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (FileUploadParser,)

    def perform_create(self, serializer):
        # Associate the user with the uploaded data
        serializer.save(user=self.request.user)