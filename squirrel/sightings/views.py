#Yipeng Niu yn2371
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.db import models
from django.template import loader
from django.forms import modelformset_factory
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pylab
from pylab import *
import pandas as pd
import PIL
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
    squirrel_list = Record.objects.order_by('id')
    template = loader.get_template('sightings/index.html')
    context = {'squirrel_list': squirrel_list}
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

#This stats function plots the general stats that are shown on /sightings/stats.
def stats(request):
    s= Record.objects.all().values()
    squirrels=pd.DataFrame(s)

    x_age = ['Adult','Juvenile', 'N/A']
    y_age = squirrels['age'].value_counts()

    x_fur = ['Gray','Cinnamon','Black','N/A']
    y_fur = squirrels['primary_fur_color'].value_counts()

    x_loc = ['Ground Plane','Above Ground','N/A']
    y_loc = squirrels['location'].value_counts()

    x_shift = squirrels['shift'].value_counts().index
    y_shift = squirrels['shift'].value_counts()

    x_run = ['False','True']
    y_run = squirrels['running'].value_counts()

    fig, axs = plt.subplots(2, 4, figsize=(30,15))
    fig.suptitle('General Stats about the Sightings', fontsize= 40)

    axs[0,0].bar(x_age, height=y_age, color=(0, 0.7, 0))
    axs[0,0].set_title('Squirrels by Age', fontsize=30)
    axs[0,0].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,0].tick_params(axis='both', which='major', labelsize=20)

    axs[0,1].bar(x_fur, height=y_fur, color=(1, 0.7, 0))
    axs[0,1].set_title('Squirrels by Primary Fur Color', fontsize=30)
    axs[0,1].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,1].tick_params(axis='both', which='major', labelsize=20)

    axs[0,2].bar(x_loc, height=y_loc, color=(0, 0, 1))
    axs[0,2].set_title('Squirrels by Location', fontsize=30)
    axs[0,2].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,2].tick_params(axis='both', which='major', labelsize=20)

    axs[0,3].bar(x_shift, height=y_shift, color=(0, 1, 0))
    axs[0,3].set_title('Squirrels by AM/PM', fontsize=30)
    axs[0,3].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,3].tick_params(axis='both', which='major', labelsize=20)

    axs[1,0].bar(x_run, height=y_run, color=(0, 0.7, 0))
    axs[1,0].set_xlabel('Running Squirrels', fontsize=25)
    axs[1,0].set_ylabel('Frequency of sightings', fontsize=25)
    axs[1,0].tick_params(axis='both', which='major', labelsize=20)


    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    return HttpResponse(buffer.getvalue(), content_type="image/png")
