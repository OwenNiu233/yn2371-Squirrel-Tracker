#Yipeng Niu yn2371
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from sighting.models import Record

def index(request):
    template = loader.get_template('map.html')
    #map.html is provided by Prof. Logston
    records = Record.objects.all()
    context = {'sighting records': records}
    return HttpResponse(template.render(context, request))
