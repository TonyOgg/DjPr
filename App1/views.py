from django.http import HttpResponse
from App1.models import Regions
from django.shortcuts import render

def starter(request):
    y = ''
    for i in Regions.objects.all():
        y = y + str(i.index) + '-' + i.name + '\n'
    return HttpResponse(y)

def sl(request):
    return HttpResponse(Regions.objects.filter(name__istartswith='G'))
