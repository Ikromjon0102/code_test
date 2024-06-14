from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures')
    gender = models.CharField(max_length=20, choices=(('male', 'Erkak'), ('female', 'Ayol')), default='male')