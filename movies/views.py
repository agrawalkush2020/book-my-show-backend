from django.shortcuts import render
from .models import City, Cinema, Show, Movie
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_all_movies(request):
    params = json.loads(request.body)
    city_name = params.get("city", "Mumbai")
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
    movies = []
    movies_list = list(movies_set)
    for movie in movies_list:
        movies.append({"id": movie.id, "name": movie.name, "rating": movie.rating})

    return HttpResponse(json.dumps({"success": True, "movies": movies}), content_type="application/json",
                        status=200)


@csrf_exempt
def get_all_locations_and_timings(request):
    params = json.loads(request.body)
    movie_id = params.get('movie_id')
    city = params.get('city')

    try:
        movie_object = Movie.objects.get(id=movie_id)
        city_object = City.objects.get(name=city)

        # Get all cinema objects in the given city that are showing the particular movie
        cinemas = Cinema.objects.filter(city=city_object, show__movie=movie_object).distinct()

        locations = [{"service_provider": "INOX", "mall": "Huda city Center", "city": "Gurugram",
                      "timings": ["10:00 AM", "09:30 PM"]}]
        for cinema in cinemas:
            # Access the service provider associated with the cinema
            service_provider = cinema.service_provider
            locations.append({"service_provider": service_provider.name, "mall": cinema.mall, "city": cinema.city,
                              "timings": []})

        return HttpResponse(json.dumps({"success": True, "locations": locations}), content_type="application/json",
                            status=200)

    except Exception as ex:
        return HttpResponse(json.dumps({"success": False, "message": ex}), content_type="application/json",
                            status=500)
