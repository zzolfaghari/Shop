from django.db import models


class UserType(models.TextChoices):
    ADMIN = "ADMIN"
    PRODUCER = "PRODUCER"
