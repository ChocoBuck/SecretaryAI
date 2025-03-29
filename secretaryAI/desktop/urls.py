from django.urls import path
from . import views

app_name = 'desktop'

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.calendar, name='calendar'),
    path('daily-schedule/', views.daily_schedule, name='daily_schedule'),
    path('tasks/', views.tasks, name='tasks'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]
