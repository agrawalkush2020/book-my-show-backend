from django.core.management.base import BaseCommand
from movies.models import City, Location, Timing, Movie


class Command(BaseCommand):
    help = 'Delete all entries from City, Location, Timing, and Movie models'

    def handle(self, *args, **kwargs):
        # Delete all entries in each model
        City.objects.all().delete()
        Location.objects.all().delete()
        Timing.objects.all().delete()
        Movie.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted all entries from City, Location, Timing, and Movie models.'))
