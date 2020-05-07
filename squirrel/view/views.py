#Yipeng Niu yn2371
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from sightings.models import Record

def index(request):
    template = loader.get_template('map.html')
    #map.html is provided by Prof. Logston
    sightings = Record.objects.all()
    sightingsshow = sightings[:100]
    context = {'sightingsshow': sightingsshow}
    return HttpResponse(template.render(context, request))
