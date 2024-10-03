import uuid
from django.db import models

# PVR, IMAX, etc
class ServiceProvider(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing id as primary key
    name = models.CharField(max_length=100, default='Unknown Provider')  # Name of the service provider
    external_eatables_allowed = models.BooleanField(default=False)  # Allowing external eatables

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique ID field
    name = models.CharField(max_length=100, default='Unknown City')  # City name
    pin_code = models.CharField(max_length=6, default='000000')  # Pin code field, assuming it's a string

    def __str__(self):
        return self.name


class Mall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique ID field
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # Foreign key linking to City model

    def __str__(self):
        return f'Mall {self.id} in {self.city.name}'


class Cinema(models.Model):
    id = models.AutoField(primary_key=True)  # id field as primary key
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    mall = models.ForeignKey(Mall, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # Foreign key linking to City
    is_multiplex = models.BooleanField(default=False)  # Indicates if it's a multiplex

    def __str__(self):
        return f'{self.service_provider} Cinema in {self.city.name}'


class Screen(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing id as primary key
    name = models.CharField(max_length=100, default='Screen 1')  # Name of the screen
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)  # Foreign key linking to Cinema
    display_name = models.CharField(max_length=100, default='Standard Screen')  # Display name

    def __str__(self):
        return f'{self.display_name} at {self.cinema.name}'


class Movie(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=200, default='Untitled Movie')  # Movie name
    actors = models.CharField(max_length=500, default='Unknown Actors')  # Comma-separated list of actors
    director = models.CharField(max_length=100, default='Unknown Director')  # Director's name
    producer = models.CharField(max_length=100, default='Unknown Producer')  # Producer's name
    duration = models.PositiveIntegerField(default=90)  # Duration in minutes, defaulting to 90
    trailer = models.TextField(blank=True, default='')  # Links to trailers
    rating = models.FloatField(default=0.0)  # Rating out of 10, defaulting to 0.0

    def __str__(self):
        return self.name


class Show(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)  # Foreign key linking to Cinema
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Foreign key linking to Movie
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)  # Foreign key linking to Screen
    start_time = models.TimeField(default='12:00:00')  # Default start time
    end_time = models.TimeField(default='14:00:00')  # Default end time
    interval_time = models.TimeField(blank=True, null=True)  # Time of interval
    interval_duration = models.PositiveIntegerField(blank=True, null=True)  # Duration of the interval in minutes

    def __str__(self):
        return f'Show of {self.movie.name} at {self.cinema.name} on {self.start_time}'
