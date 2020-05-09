from django.urls import path

from base.api import views

base_patterns_v1 = [
    path("upload/", views.upload, name="upload"),
]
