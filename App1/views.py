from django.http import HttpResponse
from App1.models import Regions
from django.shortcuts import render

def starter(request):
    return HttpResponse(Regions.objects.filter(index=1))

