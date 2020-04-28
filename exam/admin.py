from django.contrib import admin

from .models import Exam, Question, ValidAnswer, Answer


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_deleted", "created_at", "updated_at")
    search_fields = ["id", "title", "about"]
    date_hierarchy = "updated_at"


@admin.register(Question)
class QuesionAdmin(admin.ModelAdmin):
    list_display = ("id", "exam", "answer_type", "created_at", "updated_at")
    search_fields = ["id", "question_text"]
    date_hierarchy = "updated_at"


@admin.register(ValidAnswer)
class ValidAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "valid_choice", "created_at", "updated_at")
    search_fields = ["id", "question"]
    date_hierarchy = "updated_at"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "question",
        "candidate",
        "answer_text",
        "answer_choice",
        "is_valid",
        "created_at",
        "updated_at",
    )
    search_fields = ["id", "question", "candidate"]
    date_hierarchy = "updated_at"
