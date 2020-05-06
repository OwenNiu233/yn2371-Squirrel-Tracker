from django.core.management.base import BaseCommand
import pandas as pd
import csv
from sightings.models import Record


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', nargs = '+', type = str)

    def handle(self, *args, **kwargs):

        with open(kwargs['path'][0]) as file:
            reader = csv.DictReader(file)
            data = list(reader)

        for item in data:
            s = Record(
            longitude = item['X'],
            latitude = item['Y'],
            unique_squirrel_id = item['Unique Squirrel ID'],
            shift = item['Shift'],
            date = item['Date'],
            age = item['Age'],
            primary_fur_color = item['Primary Fur Color'],
            location = item['Location'],
            specific_location = item['Specific Location'],
            running = item['Running'].lower() == 'true',
            chasing = item['Chasing'].lower() == 'true',
            climbing = item['Climbing'].lower() == 'true',
            eating = item['Eating'].lower() == 'true',
            foraging = item['Foraging'].lower() == 'true',
            other_activities = item['Other Activities'],
            kuks = item['Kuks'].lower() == 'true',
            quaas = item['Quaas'].lower() == 'true',
            moans = item['Moans'].lower() == 'true',
            tail_flags = item['Tail flags'].lower() == 'true',
            tail_twitches = item['Tail twitches'].lower() == 'true',
            approaches = item['Approaches'].lower() == 'true',
            indifferent = item['Indifferent'].lower() == 'true',
            runs_from = item['Runs from'].lower() == 'true',
            )
            s.save()
