from django.db import models

from base.models import BaseModel


class Exam(BaseModel):
    title = models.CharField(max_length=500, null=True)
    about = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    techs = models.ManyToManyField("techs.Technology", related_name="exams")

    class Meta:
        app_label = "exam"

    def __str__(self):
        return self.title
