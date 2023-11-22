from django.urls import path
from .views import *

app_name = 'task_manager'
urlpatterns = [
    # path('tasks/', views.TaskListView.as_view(), name='task-list'),
    # path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    # path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    # path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('api/doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('api/tasks/', TaskListView.as_view(), name='task-list'),
]
