from django.shortcuts import render
from .models import City
from django.http import HttpResponse
import json

def get_all_locations(request):
    cities = City.objects.all()
    return HttpResponse(json.dumps({"success": True, "cities": cities}),content_type="application/json",
                        status=200)

def get_all_movies(request):

    city_name = None
    city = City.objects.get(name=city_name)
    movies = city.movies.all()  # Using the related_name 'movies' defined in the Movie model
    return HttpResponse(json.dumps({"success": True, "movies": movies}), content_type="application/json",
                        status=200)

def get_timings(request):
    city_name = None
    movie_name = None





