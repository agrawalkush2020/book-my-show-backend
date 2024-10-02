from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.address}, {self.city.name}'


class Timing(models.Model):
    start_time = models.TimeField()  # start time of the movie
    end_time = models.TimeField()    # end time of the movie

    def __str__(self):
        return f'Start: {self.start_time}, End: {self.end_time}'


class Movie(models.Model):
    name = models.CharField(max_length=100)  #done
    cities = models.ManyToManyField(City, related_name='movies')    #done
    locations = models.ManyToManyField(Location, related_name='locations')    #done
    price = models.DecimalField(max_digits=10, decimal_places=2)    #done
    timings = models.ManyToManyField(Timing, related_name='timings')   #done

    def __str__(self):
        return self.name

