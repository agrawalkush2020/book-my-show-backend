from django.core.management.base import BaseCommand
from movies.models import ServiceProvider, City, Mall, Cinema, Screen, Movie, Show
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Create Service Providers
        pvr = ServiceProvider.objects.create(name='PVR', external_eatables_allowed=True)
        imax = ServiceProvider.objects.create(name='IMAX', external_eatables_allowed=False)

        # Create Cities
        delhi = City.objects.create(name='Delhi', pin_code='110001')
        gurgaon = City.objects.create(name='Gurgaon', pin_code='122018')

        # Create Malls
        mall1 = Mall.objects.create(city=delhi)
        mall2 = Mall.objects.create(city=gurgaon)

        # Create Cinemas
        cinema1 = Cinema.objects.create(service_provider=pvr, mall=mall1, city=delhi, is_multiplex=True)
        cinema2 = Cinema.objects.create(service_provider=imax, mall=mall2, city=gurgaon, is_multiplex=False)

        # Create Screens
        screen1 = Screen.objects.create(name='Screen 1', cinema=cinema1, display_name='IMAX Screen')
        screen2 = Screen.objects.create(name='Screen 2', cinema=cinema2, display_name='Standard Screen')

        # Create Movies
        movie1 = Movie.objects.create(
            name='Avengers: Endgame',
            actors='Robert Downey Jr., Chris Evans, Scarlett Johansson',
            director='Anthony Russo',
            producer='Kevin Feige',
            duration=181,
            trailer='https://www.youtube.com/watch?v=TcMBFSGVi1c',
            rating=8.4
        )
        movie2 = Movie.objects.create(
            name='Inception',
            actors='Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page',
            director='Christopher Nolan',
            producer='Emma Thomas',
            duration=148,
            trailer='https://www.youtube.com/watch?v=YoHD9X2yJgA',
            rating=8.8
        )

        # Create Shows
        Show.objects.create(
            cinema=cinema1,
            movie=movie1,
            screen=screen1,
            start_time=timezone.now().replace(hour=14, minute=0),
            end_time=timezone.now().replace(hour=17, minute=1)
        )
        Show.objects.create(
            cinema=cinema2,
            movie=movie2,
            screen=screen2,
            start_time=timezone.now().replace(hour=18, minute=0),
            end_time=timezone.now().replace(hour=20, minute=28)
        )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
