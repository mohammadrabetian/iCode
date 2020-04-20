from django.db import models

from base.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = "accounts"

    def __str__(self):
        return self.name


class Province(BaseModel):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="provinces"
    )
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "accounts"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "country"], name="province_constraint"
            )
        ]

    def __str__(self):
        return self.name


class City(BaseModel):
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name="cities"
    )
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "accounts"
        constraints = [
            models.UniqueConstraint(fields=["name", "province"], name="city_constraint")
        ]

    def __str__(self):
        return self.name
