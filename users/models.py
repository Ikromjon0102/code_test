from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# class CustomUser(AbstractUser):
#     profile_picture = models.ImageField(upload_to='profile_pictures')
#     gender = models.CharField(max_length=20, choices=(('male', 'Erkak'), ('female', 'Ayol')), default='male')


class CustomUser(AbstractUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    # joined_date = models.DateTimeField(auto_now_add=True, default=timezone.now)
    # last_login = models.DateTimeField()

