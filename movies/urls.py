from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('get_all_locations/', admin.site.urls),
]