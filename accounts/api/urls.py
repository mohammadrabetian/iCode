from django.urls import path

from accounts.api import views

account_patterns = [
    path("user/", views.UserView.as_view()),
    path("user/change_password/", views.set_password),
]