# from .models import Movie, City, Location, Timing
# from datetime import time
#
# def get_all_movies_for_city(city='Gurugram'):
#
#     city_object = City.objects.get(name=city)
#     movies_in_gurugram = Movie.objects.filter(locations__city=city_object).prefetch_related('locations', 'timings')
#
#     output = {}
#
#
#     for movie in movies_in_gurugram:
#         print(f"Movie: {movie.name}")
#         print(f"Price: {movie.price}")
#         if output.get(movie.name) is None:
#             output[movie.name] = {'price': movie.price, 'timings': {}, 'locations': []}
#
#
#
#
#         # Get all locations in Gurugram for this movie
#         locations = movie.locations.filter(city=city_object)
#         for location in locations:
#             print(f"Location: {location.address}")
#             output[movie.name]['locations'].append(location.address)
#
#
#         # Get all timings for the movie
#         for timing in movie.timings.all():
#             print(f"Timing: Start - {timing.start_time}, End - {timing.end_time}")
#
#             output[movie.name]['timings'].update({timing.start_time.strftime("%I:%M %p"): timing.end_time.strftime("%I:%M %p")})
#         print("\n")
#     return movies_in_gurugram
#
#
