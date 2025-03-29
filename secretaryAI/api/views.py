from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def api_example(request):
    data = {'message': 'This is an API response'}
    return JsonResponse(data)
