from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # genders
    MALE = "male"
    FEMALE = "female"
    OTHER = "Other"
    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )

    phone_number = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=100, null=True, blank=True, choices=GENDERS)
    birthdate = models.DateField(null=True, blank=True)
    technology_stacks = models.ManyToManyField(
        "tech.TechnologyStack"
    )  # TODO: add TechnologyStack model
    city = models.ForeignKey(
        "accounts.City", on_delete=models.SET_NULL, null=True, blank=True
    )
    email_confirmed = models.BooleanField(default=False)

    class Meta:
        app_label = "accounts"

    def __str__(self) -> str:
        return self.get_full_name()
