#Yipeng Niu yn2371
from django.db import models
from django.utils.translation import gettext as _


class Record(models.Model):
    
    latitude = models.FloatField('Latitude', max_length = 50, default = 40.79)
    
    longitude = models.FloatField('Longitude', max_length = 50, default = -73.95)
    
    unique_squirrel_id = models.CharField('Unique Squirrel ID', max_length = 50)
    
    SHIFT_CHOICES = (
            ('AM', 'AM'),
            ('PM', 'PM')
            )
    shift = models.CharField(
            'AM or PM', 
            max_length = 2, 
            choices = SHIFT_CHOICES
            )

    date = models.IntegerField(
            'Date',
            help_text = "MMDDYYYY"
           )
    
    AGE_CHOICES = (
            ('ADULT', 'Adult'),
            ('JUVENILE', 'Juvenile')
            )
    age = models.CharField(
            'Age',
            max_length = 10,
            choices = AGE_CHOICES
            )

    PRIMARY_FUR_COLOR_CHOICES = (
            ('BLACK', 'Black'),
            ('CINNAMON', 'Cinnamon'),
            ('GRAY', 'Gray')
            )
    primary_fur_color = models.CharField(
            'Primary Fur Color',
            max_length = 10,
            choices = PRIMARY_FUR_COLOR_CHOICES
            )

    LOCATION_CHOICES = (
            ('Ground Plane', 'Ground Plane'),
            ('Above Ground', 'Above Ground')
            )
    location = models.CharField(
            'Location',
            max_length = 20,
            choices = LOCATION_CHOICES
            )
    
    specific_location = models.CharField(
            'Specific Location',
            max_length = 100
            )

    running = models.BooleanField(
            'Running',
            default = False)

    chasing = models.BooleanField(
            'Chasing',
            default = False)
    
    climbing = models.BooleanField(
            'Climbing',
            default = False)

    eating = models.BooleanField(
            'Eating',
            default = False)

    foraging = models.BooleanField(
            'foraging',
            default = False)

    other_activities = models.CharField(
            'Other Activities',
            max_length = 100
            )
    
    kuks = models.BooleanField(
            'Kuks',
            default = False)

    quaas = models.BooleanField(
            'Quaas',
            default = False)

    moans = models.BooleanField(
            'Moans',
            default = False)

    tail_flags = models.BooleanField(
            'Tail Flags',
            default = False)

    tail_twitches = models.BooleanField(
            'Tail Twitches',
            default = False)

    approaches = models.BooleanField(
            'Approaches',
            default = False)

    indifferent = models.BooleanField(
            'Indifferent',
            default = False)

    runs_from = models.BooleanField(
            'Runs from',
            default = False)

    def __str__(self):
        return ('%s' %(self.unique_squirrel_id))

