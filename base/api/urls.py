from django.urls import path

from base.api import views

base_patterns = [
    path("upload/", views.upload, name="upload"),
]
