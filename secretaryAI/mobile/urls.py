from django.urls import path
from . import views

app_name = 'mobile'

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.calendar, name='calendar'),
    path('daily_schedule/', views.daily_schedule, name='daily_schedule'),
    path('tasks/', views.tasks, name='tasks'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
