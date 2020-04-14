from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import FileModel


class User(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    image = models.ForeignKey(FileModel, null=True, on_delete=models.SET_NULL)

    class Meta:
        app_label = "accounts"

    def __str__(self) -> str:
        return self.first_name + " - " + self.last_name