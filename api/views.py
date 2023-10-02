from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from robots.models import Robot
from .models import NewRobot


def new_robots(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Robot.objects.create(
            serial=data['serial'],
            model=data['model'],
            version=data['version'],
            created=data['created']
        )
        NewRobot.objects.create(
            serial=data['serial'],
            model=data['model'],
            version=data['version'],
            created=data['created']
        )
        return JsonResponse(data)
    else:
        return HttpResponse('Wrong method. Use "POST" method to add some new robots.')
