from django.db import models 

from base.models import BaseModel


class ValidAnswer(BaseModel):
    question = models.OneToOneField("exam.Question", on_delete=models.CASCADE)
    valid_choice = models.CharField(max_length=100)

    class Meta:
        app_label = "exam"
