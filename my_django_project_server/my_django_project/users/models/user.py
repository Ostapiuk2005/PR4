from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    active = models.BooleanField(default = False)
    phone_num = models.CharField(max_length=15)

    def __str__(self):
        return self.username