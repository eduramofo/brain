from django.shortcuts import render
from django.http import JsonResponse


def hello(request):
    data = {
        'success': True    
    }
    return JsonResponse(data)
