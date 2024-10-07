import random
from django.core.management.base import BaseCommand
from movies.models import ServiceProvider, City, Mall, Cinema, Screen, Movie, Show
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create Service Providers
        providers = [
            ServiceProvider(name='PVR', external_eatables_allowed=True),
            ServiceProvider(name='IMAX', external_eatables_allowed=False),
            ServiceProvider(name='Inox', external_eatables_allowed=False)
        ]
        ServiceProvider.objects.bulk_create(providers)
        self.stdout.write(self.style.SUCCESS('Service providers created.'))

        # Create Cities
        cities = [
            City(name='New Delhi', pin_code='110001'),
            City(name='Mumbai', pin_code='400001'),
            City(name='Bangalore', pin_code='560001')
        ]
        City.objects.bulk_create(cities)
        self.stdout.write(self.style.SUCCESS('Cities created.'))

        # Create Malls
        malls = [
            Mall(city=cities[0]),
            Mall(city=cities[1]),
            Mall(city=cities[2]),
        ]
        Mall.objects.bulk_create(malls)
        self.stdout.write(self.style.SUCCESS('Malls created.'))

        # Create Cinemas
        cinemas = [
            Cinema(service_provider=providers[0], mall=malls[0], city=cities[0], is_multiplex=True),
            Cinema(service_provider=providers[1], mall=malls[1], city=cities[1], is_multiplex=False),
            Cinema(service_provider=providers[2], mall=malls[2], city=cities[2], is_multiplex=True),
        ]
        Cinema.objects.bulk_create(cinemas)
        self.stdout.write(self.style.SUCCESS('Cinemas created.'))

        # Create Screens
        screens = [
            Screen(name='Screen 1', cinema=cinemas[0], display_name='IMAX 3D Screen'),
            Screen(name='Screen 2', cinema=cinemas[1], display_name='Dolby Cinema'),
            Screen(name='Screen 3', cinema=cinemas[2], display_name='4DX Screen')
        ]
        Screen.objects.bulk_create(screens)
        self.stdout.write(self.style.SUCCESS('Screens created.'))

        # Create Movies
        movies = [
            Movie(name='The Matrix', actors='Keanu Reeves, Laurence Fishburne', director='Wachowskis', producer='Joel Silver', duration=136, trailer='https://youtube.com/matrix', rating=8.7),
            Movie(name='Inception', actors='Leonardo DiCaprio, Joseph Gordon-Levitt', director='Christopher Nolan', producer='Emma Thomas', duration=148, trailer='https://youtube.com/inception', rating=8.8),
            Movie(name='Interstellar', actors='Matthew McConaughey, Anne Hathaway', director='Christopher Nolan', producer='Emma Thomas', duration=169, trailer='https://youtube.com/interstellar', rating=8.6)
        ]
        Movie.objects.bulk_create(movies)
        self.stdout.write(self.style.SUCCESS('Movies created.'))

        # Create Shows
        show_time = datetime.now()
        shows = [
            Show(cinema=cinemas[0], movie=movies[0], screen=screens[0], start_time=show_time, end_time=show_time + timedelta(hours=2)),
            Show(cinema=cinemas[1], movie=movies[1], screen=screens[1], start_time=show_time, end_time=show_time + timedelta(hours=2)),
            Show(cinema=cinemas[2], movie=movies[2], screen=screens[2], start_time=show_time, end_time=show_time + timedelta(hours=3))
        ]
        Show.objects.bulk_create(shows)
        self.stdout.write(self.style.SUCCESS('Shows created.'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
