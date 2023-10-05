from django.urls import path
from . import views

urlpatterns = [
    # Your existing URL patterns
    path('sleeplog/create/', views.SleepLogCreate.as_view(), name='sleeplog-create'),
    path('sleeplog/list/', views.SleepLogList.as_view(), name='sleeplog-list'),
    path('sensordata/create/', views.SensorDataCreateView.as_view(), name='sensordata-create'),

]