from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return HttpResponse('''
    <h1>Welcome to Squirrel Tracker by yn2371.</h1>
    <h2><a href = "/map/">Click here to see a map that displays the location of the squirrel sightings.</a></h2>
    <h2><a href = "/sightings/">Click here to see a list of all squirrel sightings.</a></h2>
    ''')
