from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.handle_signup),
    path('login/', views.handle_login),
    path('logout/',views.handle_logout),
]
