# Generated by Django 3.0.6 on 2020-05-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=40.79, max_length=50, verbose_name='Latitude')),
                ('longitude', models.FloatField(default=-73.95, max_length=50, verbose_name='Longitude')),
                ('unique_squirrel_id', models.CharField(max_length=50, verbose_name='Unique Squirrel ID')),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2, verbose_name='AM or PM')),
                ('date', models.IntegerField(help_text='MMDDYYYY', verbose_name='Date')),
                ('age', models.CharField(choices=[('ADULT', 'Adult'), ('JUVENILE', 'Juvenile')], max_length=10, verbose_name='Age')),
                ('primary_fur_color', models.CharField(choices=[('BLACK', 'Black'), ('CINNAMON', 'Cinnamon'), ('GRAY', 'Gray')], max_length=10, verbose_name='Primary Fur Color')),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=20, verbose_name='Location')),
                ('specific_location', models.CharField(max_length=100, verbose_name='Specific Location')),
                ('running', models.BooleanField(default=False, verbose_name='Running')),
                ('chasing', models.BooleanField(default=False, verbose_name='Chasing')),
                ('climbing', models.BooleanField(default=False, verbose_name='Climbing')),
                ('eating', models.BooleanField(default=False, verbose_name='Eating')),
                ('foraging', models.BooleanField(default=False, verbose_name='foraging')),
                ('other_activities', models.CharField(max_length=100, verbose_name='Other Activities')),
                ('Kuks', models.BooleanField(default=False, verbose_name='Kuks')),
                ('quaas', models.BooleanField(default=False, verbose_name='Quaas')),
                ('moans', models.BooleanField(default=False, verbose_name='Moans')),
                ('tail_flags', models.BooleanField(default=False, verbose_name='Tail Flags')),
                ('tail_twitches', models.BooleanField(default=False, verbose_name='Tail Twitches')),
                ('approaches', models.BooleanField(default=False, verbose_name='Approaches')),
                ('indifferent', models.BooleanField(default=False, verbose_name='Indifferent')),
                ('runs_from', models.BooleanField(default=False, verbose_name='Runs from')),
            ],
        ),
    ]
