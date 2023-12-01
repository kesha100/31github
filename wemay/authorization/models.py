from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import MyUserManager
from .utils import user_image_path


# Create your models here.


class MyUser(AbstractUser):
    """self custom user"""
    username = models.CharField(unique=True, max_length=100, null=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to=user_image_path, default=None, blank=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    REQUIRED_FIELDS = ['email']

    objects = MyUserManager()

    def __str__(self):
        return self.email


