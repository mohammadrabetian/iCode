from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = "accounts"

    def __str__(self) -> str:
        return self.get_full_name()
