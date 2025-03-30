from django.shortcuts import render

def home(request):
    return render(request, 'desktop/home.html')

def calendar(request):
    return render(request, 'desktop/calendar.html')

def daily_schedule(request):
    return render(request, 'desktop/daily_schedule.html')

def tasks(request):
    return render(request, 'desktop/tasks.html')

def notifications(request):
    return render(request, 'desktop/notifications.html')

def profile(request):
    return render(request, 'desktop/profile.html')

def settings(request):
    return render(request, 'desktop/settings.html')

def chatbot(request):
    return render(request, 'desktop/chatbot.html')