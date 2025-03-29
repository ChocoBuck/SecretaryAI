from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('example/', views.api_example, name='example'),
]
