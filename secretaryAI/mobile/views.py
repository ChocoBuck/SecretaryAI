from django.shortcuts import render

def home(request):
    return render(request, 'mobile/home.html')

def calendar(request):
    return render(request, 'mobile/calendar.html')

def daily_schedule(request):
    return render(request, 'mobile/daily_schedule.html')

def tasks(request):
    return render(request, 'mobile/tasks.html')

def notifications(request):
    return render(request, 'mobile/notifications.html')

def profile(request):
    return render(request, 'mobile/profile.html')

def settings(request):
    return render(request, 'mobile/settings.html')

def chatbot(request):
    return render(request, 'mobile/chatbot.html')
