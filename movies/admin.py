from django.contrib import admin
from .models import ServiceProvider, City, Mall, Cinema, Screen, Movie, Show

# Register your models here.
admin.site.register(ServiceProvider)
admin.site.register(City)
admin.site.register(Mall)
admin.site.register(Cinema)
admin.site.register(Screen)
admin.site.register(Movie)
admin.site.register(Show)