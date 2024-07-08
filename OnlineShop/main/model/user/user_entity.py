from django.contrib.auth.models import AbstractUser
from django.db import models

from main.enum.user_type import UserType


class User(AbstractUser):
    email = models.EmailField(max_length=80, unique=True, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    type = models.CharField(max_length=20, choices=UserType.choices)