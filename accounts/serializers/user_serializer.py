from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from accounts.models import User


class CreateUserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    full_name = serializers.SerializerMethodField("get_full_name", read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    def save(self):
        self.validated_data['password'] = make_password(self.validated_data.get("password"))
        return super(CreateUserSerializer, self).save()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def get_full_name(self, obj):
        if obj.first_name and obj.last_name:
            return obj.first_name + " " + obj.last_name
        elif obj.first_name or obj.last_name:
            return obj.first_name if obj.first_name else obj.last_login
        else:
            return None
