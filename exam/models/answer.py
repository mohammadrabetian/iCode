from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from base.models import BaseModel


class Answer(BaseModel):
    question = models.ForeignKey(
        "exam.Question", on_delete=models.CASCADE, related_name="answers"
    )
    candidate = models.ForeignKey(
        "accounts.Candidate", on_delete=models.DO_NOTHING, related_name="answers"
    )
    answer_text = models.TextField(null=True, blank=True)
    answer_choice = models.CharField(max_length=100, null=True, blank=True)
    # for choice field questions
    is_valid = models.NullBooleanField()
    # for text field questions
    satisfactory_rate = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], default=0
    )

    class Meta:
        app_label = "exam"
