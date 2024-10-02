import uuid
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='locations')  # ForeignKey to City

    def __str__(self):
        return f'{self.address}'


class Timing(models.Model):
    start_time = models.TimeField()  # start time of the movie
    end_time = models.TimeField()    # end time of the movie

    def __str__(self):
        return f'Start: {self.start_time}, End: {self.end_time}'


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique ID field
    name = models.CharField(max_length=100)
    cities = models.ManyToManyField(City, related_name='movies')
    locations = models.ManyToManyField(Location, related_name='locations')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timings = models.ManyToManyField(Timing, related_name='timings')

    def __str__(self):
        return self.name
