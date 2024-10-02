from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)  # Ensuring email uniqueness

    # Add unique related_name attributes for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='customuser'
    )

    def __str__(self):
        return self.username

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