import uuid
from django.core.management.base import BaseCommand
from movies.models import City, Location, Timing, Movie


class Command(BaseCommand):
    help = 'Populate the database with sample movie data, including new locations and timings for Gurugram'

    def handle(self, *args, **kwargs):
        # Create or get sample cities
        city1, _ = City.objects.get_or_create(name='New York')
        city2, _ = City.objects.get_or_create(name='Los Angeles')
        city3, _ = City.objects.get_or_create(name='Chicago')
        city4, _ = City.objects.get_or_create(name='Houston')
        city5, _ = City.objects.get_or_create(name='Phoenix')
        city6, _ = City.objects.get_or_create(name='Gurugram')  # New city Gurugram

        # Create or get sample locations
        location1, _ = Location.objects.get_or_create(address='123 Broadway, NY', city=city1)
        location2, _ = Location.objects.get_or_create(address='456 Sunset Blvd, LA', city=city2)
        location3, _ = Location.objects.get_or_create(address='789 Michigan Ave, Chicago', city=city3)
        location4, _ = Location.objects.get_or_create(address='101 Main St, Houston', city=city4)
        location5, _ = Location.objects.get_or_create(address='202 Central Ave, Phoenix', city=city5)

        # New locations for Gurugram
        gurugram_locations = [
            Location.objects.get_or_create(address='10 Cyber Hub, Gurugram', city=city6)[0],
            Location.objects.get_or_create(address='15 Sector 29, Gurugram', city=city6)[0],
            Location.objects.get_or_create(address='8 Golf Course Road, Gurugram', city=city6)[0],
            Location.objects.get_or_create(address='5 Sohna Road, Gurugram', city=city6)[0],
        ]

        # Create or get sample timings
        timing1, _ = Timing.objects.get_or_create(start_time='10:00', end_time='12:00')
        timing2, _ = Timing.objects.get_or_create(start_time='14:00', end_time='16:00')
        timing3, _ = Timing.objects.get_or_create(start_time='18:00', end_time='20:00')
        timing4, _ = Timing.objects.get_or_create(start_time='20:30', end_time='22:30')
        timing5, _ = Timing.objects.get_or_create(start_time='23:00', end_time='01:00')

        # New timings for Gurugram
        gurugram_timings = [
            Timing.objects.get_or_create(start_time='09:00', end_time='11:00')[0],
            Timing.objects.get_or_create(start_time='13:00', end_time='15:00')[0],
            Timing.objects.get_or_create(start_time='17:00', end_time='19:00')[0],
            Timing.objects.get_or_create(start_time='21:00', end_time='23:00')[0],
        ]

        # Create or get sample movies with the new Gurugram data
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
            {
                'name': 'Movie 6',
                'cities': [city6],  # Gurugram
                'locations': gurugram_locations,
                'price': 15.99,
                'timings': gurugram_timings,
            },
        ]

        for movie_data in movies_data:
            movie, created = Movie.objects.get_or_create(
                name=movie_data['name'],
                price=movie_data['price'],
            )

            if created:
                movie.cities.set(movie_data['cities'])
                movie.locations.set(movie_data['locations'])
                movie.timings.set(movie_data['timings'])
            else:
                # Avoid duplicate timings and locations
                movie.cities.add(*movie_data['cities'])
                movie.locations.add(*movie_data['locations'])
                for timing in movie_data['timings']:
                    if timing not in movie.timings.all():
                        movie.timings.add(timing)

        self.stdout.write(
            self.style.SUCCESS('Successfully populated the database with movie data, including Gurugram.'))
