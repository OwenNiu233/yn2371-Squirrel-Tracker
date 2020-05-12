from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return HttpResponse('''
    <!doctype html>
<html lang="en">
	<head>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

		<title>Home Page</title>
	</head>
	<body>
		<nav class="navbar navbar-expand-lg navbar-light bg-light">
			<a class="navbar-brand" href="">SquaTra yn2371		</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon">		</span>
			</button>

			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav mr-auto">
					<li class="nav-item active">
						<a class="nav-link" href="">Home 		<span class="sr-only">(current)		</span>		</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="/map/">Map		</a>
					</li>
					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
					Sightings
						</a>
						<div class="dropdown-menu" aria-labelledby="navbarDropdown">
							<a class="dropdown-item" href="/sightings/add/">Add		</a>
							<a class="dropdown-item" href="/sightings/stats/">Stats		</a>
							<div class="dropdown-divider">		</div>
							<a class="dropdown-item" href="/sightings/">Sightings		</a>
						</div>
					</li>
				</ul>
			</div>
		</nav>
                <h1>Welcome to Squirrel Tracker by yn2371.</h1>
		<ul class="list-group">
			<li class="list-group-item"><a href = "/map/">Click here to see a map that displays the location of the squirrel sightings.</a></li>
			<li class="list-group-item"><a href = "/sightings/">Click here to see a list of all squirrel sightings.</a></li>
		</ul>
		<div class="card">
			<div class="card-body">
				This is an IEOR4501 Tools for Analytics project. The project is Django-based and tracks squirrels.
			</div>
			<div class="card-body">
				You can find the GitHub page of this project <a href = "https://github.com/OwenNiu233/yn2371-Squirrel-Tracker.git">here</a>.
			</div>
			<div class="card-body">
				Eccentric billionaire Joffrey Hosencratz just purchased the web development company I work for. I’ve met him once in an elevator and he was impressed with my skill in developing web applications with the Django framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. He would like to start keeping track of all the known squirrels and plans to start with Central Park. He asked me to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data.
			</div>
		</div>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
	</body>
</html>
        ''')

