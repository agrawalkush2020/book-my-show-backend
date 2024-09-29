from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    # profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username

    @classmethod
    def is_existing_user(cls, username=None, email=None, phone_number=None):
        """
        Check if there is an existing user with the given username, email, or phone number.
        """
        if username:
            if cls.objects.filter(username=username).exists():
                return True
        if email:
            if cls.objects.filter(email=email).exists():
                return True
        if phone_number:
            if cls.objects.filter(phone_number=phone_number).exists():
                return True
        return False