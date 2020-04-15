from django.contrib import admin

from .models import Exam, Question

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_deleted", "created_at", "updated_at")
    search_fields = ["id", "title", "about"]
    date_hierarchy = "updated_at"

@admin.register(Question)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("id", "exam", "answer_type", "created_at", "updated_at")
    search_fields = ["id", "question_text"]
    date_hierarchy = "updated_at"

