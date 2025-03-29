from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calendar(request):
    return render(request, 'calendar.html')

def daily_schedule(request):
    return render(request, 'daily_schedule.html')

def tasks(request):
    return render(request, 'tasks.html')

def notifications(request):
    return render(request, 'notifications.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')
