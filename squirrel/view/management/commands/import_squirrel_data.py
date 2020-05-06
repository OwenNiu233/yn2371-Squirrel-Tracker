import csv
#Original by Prof. Logston
#modified by Yipeng Niu
from django.core.management.base import BaseCommand
from django.utils import timezone
from sightings.models import Record
import pandas as pd

class Command(BaseCommand):
    help = 'Import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

            for item in data:
                s = Record(
                latitude=float(item['Y']),
                longitude=float(item['X']),
                unique_squirrel_id=item['Unique Squirrel ID'],
                shift=item['Shift'].lower(),
                date=timezone.datetime.strptime(item['Date'], '%m%d%Y').date(),
                age=item['Age'],
                primary_fur_color=item['Primary Fur Color'],
                specific_location=item['Specific Location'],
                running=item['Running'].lower() == 'true',
                chasing=item['Chasing'].lower() == 'true',
                climbing=item['Climbing'].lower() == 'true',
                eating=item['Eating'].lower() == 'true',
                foraging=item['Foraging'].lower() == 'true',
                other_activities=item['Other Activities'],
                kuks=item['Kuks'].lower() == 'true',
                quaas=item['Quaas'].lower() == 'true',
                moans=item['Moans'].lower() == 'true',
                tail_flags=item['Tail flags'].lower() == 'true',
                tail_twitches=item['Tail twitches'].lower() == 'true',
                approaches=item['Approaches'].lower() == 'true',
                indifferent=item['Indifferent'].lower() == 'true',
                runs_from=item['Runs from'].lower() == 'true',
                )
                s.save
