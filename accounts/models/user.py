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
    job_title = models.ForeignKey(
        "jobs.JobTitle", on_delete=models.SET_NULL, null=True, blank=True
    )  # TODO: jobs title model
    city = models.ForeignKey(
        "accounts.City", on_delete=models.SET_NULL, null=True, blank=True
    )  # TODO: city model
    email_confirmed = models.BooleanField(default=False)

    class Meta:
        app_label = "accounts"

    def __str__(self) -> str:
        return self.get_full_name()
