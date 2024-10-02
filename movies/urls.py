from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('get_all_locations/', views.get_all_locations),
    path('get_all_movies/', views.get_all_movies),

]