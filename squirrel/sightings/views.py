#Yipeng Niu yn2371
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.db import models
from django.template import loader
from django.forms import modelformset_factory
from django.db.models import Avg, Max, Min, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd
from io import BytesIO
from .models import Record
from .forms import RecordForm


def s_id(request, user_id):
    data = Record.objects.get(unique_squirrel_id = user_id) 
    if request.method == 'POST':
        form = RecordForm(request.POST, instance = data)
        if form.is_valid():
            form.save(commit = True)
            return HttpResponseRedirect('/sightings/')
    else:
        form = RecordForm(instance = data)
    return render(request, 'sightings/update.html', {'form': form})

def index(request):
    s_list = Record.objects.order_by('id')
    template = loader.get_template('sightings/index.html')
    context = {'s_list': s_list}
    return HttpResponse(template.render(context, request))

def add(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = RecordForm()
    return render(request, 'sightings/add.html', {'form':form})

def stats(request):
    sq_data = Record.objects.all()
    a = len(sq_data)
    b = sq_data.aggregate(
            min_latitude=Min('latitude'),
            max_latitude=Max('latitude'),
            average_latitude=Avg('latitude')
            )
    c = sq_data.aggregate(
            min_longitude=Min('longitude'),
            max_longitude=Max('longitude'),
            average_longitude=Avg('longitude')
            )
    d = list(sq_data.values_list('shift').annotate(Count('shift')))
    e = list(sq_data.values_list('age').annotate(Count('age')))
    f = list(sq_data.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    return render(request, 'sightings/stats.html', {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f})
