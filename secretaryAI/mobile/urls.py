from django.urls import path
from . import views

app_name = 'mobile'

urlpatterns = [
    path('', views.mobile_home, name='home'),
]
