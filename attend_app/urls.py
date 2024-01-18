# attendance_app/urls.py
from django.urls import path
from .views import start_attendance, end_attendance, calculate_working_hours,home

urlpatterns = [
    path('', home , name='home'),

    path('start/', start_attendance, name='start_attendance'),
    path('end/', end_attendance, name='end_attendance'),
    path('total_hours/', calculate_working_hours, name='calculate_working_hours'),
]