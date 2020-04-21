from django.db import models

from base.models import BaseModel


class Candidate(BaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    profile_image = models.OneToOneField(
        "base.File", on_delete=models.SET_NULL, null=True, blank=True
    )
    github_link = models.URLField(max_length=1000, null=True, blank=True)
    expected_salary = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        app_label = "accounts"

    def __str__(self):
        return self.user.username
