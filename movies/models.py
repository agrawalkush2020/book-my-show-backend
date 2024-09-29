from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return f'{self.address}, {self.city.name}'

class Movie(models.Model):
    name = models.CharField(max_length=100)
    cities = models.ManyToManyField(City, related_name='movies')
    locations = models.ManyToManyField(Location, related_name='locations')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name
