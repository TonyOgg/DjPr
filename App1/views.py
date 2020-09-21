from django.http import HttpResponse
from App1.models import Regions
from django.shortcuts import render
import datetime

def starter(request):
    y = ''
    for i in Regions.objects.all():
        y = y + str(i.index) + '-' + i.name + '\n'
    return HttpResponse(y)

def sl(request):
    return HttpResponse(Regions.objects.filter(name__istartswith='G'))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def page(request):
    context = {
        'header': 'Меню',
        'menu': [
            'Каталог',
            'О нас',
            'admin'
        ]
    }
    return render(request, 'index.html', context)
