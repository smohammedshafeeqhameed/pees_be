from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models.signals import pre_save
import json

class SleepLogCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.user)
        try:
            payload = json.loads(request.body)

            # Extract data from the payload
            date = payload.get('date')
            day_of_week = payload.get('dayofWeek')
            bedtime = payload.get('bedTime')
            wake_up_time = payload.get('wakeupTime')
            sleep_duration = payload.get('sleepDuration')
            sleep_environment = payload.get('sleepEnvironment')
            pre_sleep_routine = payload.get('preSleepRoutine')
            quality_of_sleep = payload.get('qualityRateSleep')
            naps = payload.get('DaytimeNaps')
            sleep_disturbances = payload.get('sleepDisturbances')
            dreams_or_nightmares = payload.get('dreams')
            feeling_upon_waking = payload.get('feelingUponWaking')
            difficulty_falling_asleep = payload.get('difficultyFallingAsleepRate')
            difficulty_staying_asleep = payload.get('difficultyStayingAsleepRate')
            problems_waking_up_early = payload.get('problemsOnWakingUpRate')
            satisfaction_with_sleep = payload.get('satisfySleepRate')
            noticeable_impairment = payload.get('sleepProblemsRate')
            worried_distressed = payload.get('sleepDistressedRate')
            interference_with_daily_functioning = payload.get('sleepDailyFunctionalRate')
            naps_duration_hour = payload.get('napsDuration', {}).get('hour', 0)
            naps_duration_minutes = payload.get('napsDuration', {}).get('minutes', 0)

            # Create SleepLog instance
            sleep_log = SleepLog(
                user=request.user,
                date=date,
                day_of_week=day_of_week,
                bedtime=bedtime,
                wake_up_time=wake_up_time,
                total_sleep_duration=sleep_duration,
                sleep_environment=sleep_environment,
                pre_sleep_routine=pre_sleep_routine,
                quality_of_sleep=quality_of_sleep,
                naps=naps,
                sleep_disturbances=sleep_disturbances,
                dreams_or_nightmares=dreams_or_nightmares,
                feeling_upon_waking=feeling_upon_waking,
                difficulty_falling_asleep=difficulty_falling_asleep,
                difficulty_staying_asleep=difficulty_staying_asleep,
                problems_waking_up_early=problems_waking_up_early,
                satisfaction_with_sleep=satisfaction_with_sleep,
                noticeable_impairment=noticeable_impairment,
                worried_distressed=worried_distressed,
                interference_with_daily_functioning=interference_with_daily_functioning,
                naps_duration_hour=naps_duration_hour,
                naps_duration_minutes=naps_duration_minutes,
            )

            # Save SleepLog instance
            sleep_log.save()
            # sleep_log.calculate_total_score()

            # Save SleepLog instance again after calculating total score
            # sleep_log.save()
            return Response({"message: Successfully created SleepLog"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
# @receiver(pre_save, sender=SleepLog)
# def update_total_score(sender, instance, **kwargs):
#     instance.calculate_total_score()
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