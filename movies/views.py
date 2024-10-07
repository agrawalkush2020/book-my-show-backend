from django.shortcuts import render
from .models import City, Cinema, Show
from django.http import HttpResponse
import json


def get_all_movies(request):
    params = json.loads(request.body)

    city_name = params.get("city", "Gurugram")
    city = City.objects.get(name=city_name)

    cinemas = Cinema.objects.filter(city=city)
    # Set to store unique movies
    movies_set = set()
    # Iterate through cinemas and their shows to gather movies
    for cinema in cinemas:
        shows = Show.objects.filter(cinema=cinema)
        for show in shows:
            movies_set.add(show.movie)  # Add movie to the set

    # Convert the set back to a list (if needed)
    movies = list(movies_set)
    for movie in movies:




    return HttpResponse(json.dumps({"success": True, "movies": movies}), content_type="application/json",
                        status=200)




