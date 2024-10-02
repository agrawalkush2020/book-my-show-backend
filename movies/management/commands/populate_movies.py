import uuid
from django.core.management.base import BaseCommand
from movies.models import City, Location, Timing, Movie


class Command(BaseCommand):
    help = 'Populate the database with sample movie data'

    def handle(self, *args, **kwargs):
        # Create sample cities
        city1 = City.objects.create(name='New York')
        city2 = City.objects.create(name='Los Angeles')
        city3 = City.objects.create(name='Chicago')
        city4 = City.objects.create(name='Houston')
        city5 = City.objects.create(name='Phoenix')

        # Create sample locations
        location1 = Location.objects.create(address='123 Broadway, NY', city=city1)
        location2 = Location.objects.create(address='456 Sunset Blvd, LA', city=city2)
        location3 = Location.objects.create(address='789 Michigan Ave, Chicago', city=city3)
        location4 = Location.objects.create(address='101 Main St, Houston', city=city4)
        location5 = Location.objects.create(address='202 Central Ave, Phoenix', city=city5)

        # Create sample timings
        timing1 = Timing.objects.create(start_time='10:00', end_time='12:00')
        timing2 = Timing.objects.create(start_time='14:00', end_time='16:00')
        timing3 = Timing.objects.create(start_time='18:00', end_time='20:00')
        timing4 = Timing.objects.create(start_time='20:30', end_time='22:30')
        timing5 = Timing.objects.create(start_time='23:00', end_time='01:00')

        # Create sample movies with the sample cities, locations, and timings
        movies_data = [
            {
                'name': 'Movie 1',
                'cities': [city1, city2],
                'locations': [location1, location2],
                'price': 10.99,
                'timings': [timing1, timing2],
            },
            {
                'name': 'Movie 2',
                'cities': [city3],
                'locations': [location3],
                'price': 12.99,
                'timings': [timing3, timing4],
            },
            {
                'name': 'Movie 3',
                'cities': [city4],
                'locations': [location4],
                'price': 9.99,
                'timings': [timing1, timing5],
            },
            {
                'name': 'Movie 4',
                'cities': [city5],
                'locations': [location5],
                'price': 14.99,
                'timings': [timing2, timing3],
            },
            {
                'name': 'Movie 5',
                'cities': [city1, city3, city4],
                'locations': [location1, location3, location4],
                'price': 11.99,
                'timings': [timing4, timing5],
            },
        ]

        for movie_data in movies_data:
            movie = Movie.objects.create(
                name=movie_data['name'],
                price=movie_data['price'],
            )
            movie.cities.set(movie_data['cities'])
            movie.locations.set(movie_data['locations'])
            movie.timings.set(movie_data['timings'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with movie data.'))

