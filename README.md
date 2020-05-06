# yn2371-Squirrel-Tracker
An IEOR4501 Tools for Analytics project. The project is Django-based and tracks squirrels.

The following contents are paraphrased or copied from [*Squirrel Tracker*](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit), the project description.

The website is http://35.192.201.79/.

The totally true background story
------------------------------------
Eccentric billionaire Joffrey Hosencratz just purchased the web development company I work for. I’ve met him once in an elevator and he was impressed with my skill in developing web applications with the Django framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He asked me to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data. 


Contributor
--------------------------------------
### Project Group 2, Section 1

UNIs: [yn2371]

Yipeng Niu yn2371


Features
--------------------------------------
Management commands:
* Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
	$ python manage.py import_squirrel_data /path/to/file.csv
	The squirrel census file can be downloaded here: https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv
* Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
	$ python manage.py export_squirrel_data /path/to/file.csv

Views:
* A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.
  * Located at: /map
  * Methods Supported: GET
  * Will use the https://leafletjs.com/ library for plotting
  * Please note: Your browser will start to freeze if you plot more than 100 points at once. We will assume our client is okay with this plotting issue.
  * You can find the HTML template I used here: https://gist.github.com/logston/0b6f2cbb928a386decd63fd616d084dd
* A view that lists all squirrel sightings with links to view each sighting
  * Located at: /sightings
  * Methods Supported: GET
  * Fields to show:
    * Unique Squirrel ID
    * Date
  * Link to unique squirrel sighting
  * This view also has a single link to the “add” sighting view
* A view to update a particular sighting
  * Located at: /sightings/<unique-squirrel-id>
  * Methods Supported: GET & POST
  * Fields to show:
    * Latitude
    * Longitude
    * Unique Squirrel ID
    * Shift
    * Date
    * Age
* A view to create a new sighting
  * Located at: /sightings/add
  * Methods Supported: GET & POST
  * Fields supported:
    * Latitude
    * Longitude
    * Unique Squirrel ID
    * Shift
    * Date
    * Age
    * Primary Fur Color
    * Location
    * Specific Location
    * Running
    * Chasing
    * Climbing
    * Eating
    * Foraging
    * Other Activities
    * Kuks
    * Quaas
    * Moans
    * Tail flags
    * Tail twitches
    * Approaches
    * Indifferent
    * Runs from
* A view with general stats about the sightings
  * Particular stats are for you to decide but must include five of the attributes listed in the initial CSV download. 
  * Located at: /sightings/stats
  * Method: GET

Data validation happens at all points of data ingestion.
