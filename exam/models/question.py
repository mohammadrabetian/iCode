from django.db import models

from base.models import BaseModel
from exam.models import Exam


class Question(BaseModel):
    VIDEO = "video"
    VOICE = "voice"
    FILE = "file"
    TEXT = "text"
    CHOICE = "choice"
    MULTI_CHOICE = "multi_choice"
    ANSWER_TYPES = (
        (VIDEO, "Video"),
        (VOICE, "Voice"),
        (FILE, "File"),
        (TEXT, "Text"),
        (CHOICE, "Choice"),
        (MULTI_CHOICE, "Multi Choice"),
    )
    exam = models.ForeignKey(
        Exam, null=True, on_delete=models.SET_NULL, related_name="questions"
    )
    answer_type = models.CharField(max_length=1000, choices=ANSWER_TYPES)
    answer_choices = models.CharField(null=True, blank=True, max_length=1000)
    question_text = models.TextField(null=True, blank=True)
    other_details = models.TextField(null=True, blank=True)

    class Meta:
        app_label = "exam"

    def __str__(self):
        return self.question_text
