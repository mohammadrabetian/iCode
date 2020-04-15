from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from accounts.models import User


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    def save(self):
        self.validated_data['password'] = make_password(self.validated_data.get("password"))
        return super(CreateUserSerializer, self).save()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

