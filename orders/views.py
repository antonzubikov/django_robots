from django.shortcuts import render
import json
from robots.models import Robot
from django.http import HttpResponse, JsonResponse


data = None


def create_order(request):
    if request.method == 'POST':
        global data
        data = json.loads(request.body)
        exist = Robot.objects.filter(model=data['model']).filter(version=data['version']).all()
        if not exist:
            return HttpResponse(f'Простите, сейчас такого робота нет в наличии. Мы сообщим вам о его поступлении.')
        else:
            return JsonResponse(data)
