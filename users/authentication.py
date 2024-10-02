from django.contrib.auth.backends import ModelBackend
from .models import CustomUser  # Adjust the import based on your user model


class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None