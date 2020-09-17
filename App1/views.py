from django.shortcuts import render
from django.http import HttpResponse
from App1.models import Regions

def starter(request):
    p = ''
    for n in Regions.objects.all():
        p = p + n.name + ' ' + str(n.index) + ' '
    return HttpResponse(p)

