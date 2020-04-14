from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "is_active", "last_login")
    search_fields = ["first_name", "last_name", "email"]
    date_hierarchy = "last_login"
