"""
URL configuration for secretaryAI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def device_dispatch(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    # A simple check; you can refine this logic as needed.
    if "mobile" in user_agent:
        return redirect('mobile:home')
    else:
        return redirect('desktop:home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', device_dispatch, name='home_dispatch'),
    path('mobile/', include('mobile.urls')),
    path('desktop/', include('desktop.urls')),
    path('api/', include('api.urls')),
]
