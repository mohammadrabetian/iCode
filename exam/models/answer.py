from django.db import models

from base.models import BaseModel


class Answer(BaseModel):
    question = models.ForeignKey(
        "exam.Question", on_delete=models.CASCADE, related_name="answers"
    )
    candidate = models.ForeignKey(
        "accounts.Candidate", on_delete=models.DO_NOTHING, related_name="answers"
    )
    answer_text = models.TextField(null=True, blank=True)
    answer_choice = models.CharField(null=True, blank=True)
    is_valid = models.NullBooleanField()

    class Meta:
        app_label = "exam"
