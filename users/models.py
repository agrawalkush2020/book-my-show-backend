from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# super user
# id: kush
# password: kush

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, unique=False)
    email = models.EmailField(unique=True)  # Ensuring email uniqueness



    def __str__(self):
        return f'{self.phone_number} - {self.email}'

    @classmethod
    def is_existing_user(cls, username=None, email=None, phone_number=None):
        """
        Check if there is an existing user with the given username, email, or phone number.
        """
        if email:
            if cls.objects.filter(email=email).exists():
                return True
        if phone_number:
            if cls.objects.filter(phone_number=phone_number).exists():
                return True
        return False