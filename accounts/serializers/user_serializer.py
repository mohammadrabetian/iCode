from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from accounts.models import User


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.RegexField(regex="\+\d{12}", allow_blank=False)
    gender = serializers.ChoiceField(choices=["male", "female", "other"], allow_blank=False)
    birth_date = serializers.DateField(input_formats=["%Y-%m-%d"], format="%Y-%m-%d")
    
    def save(self):
        self.validated_data["password"] = make_password(
            self.validated_data.get("password")
        )
        return super(CreateUserSerializer, self).save()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class EditUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.RegexField(regex="\+\d{12}", allow_blank=False, required=False)
    gender = serializers.ChoiceField(choices=["male", "female", "other"], allow_blank=False, required=False)
    birth_date = serializers.DateField(input_formats=["%Y-%m-%d"], format="%Y-%m-%d", required=False)
    
    def save(self):
        self.validated_data["password"] = make_password(
            self.validated_data.get("password")
        )
        return super(CreateUserSerializer, self).save()

    def create(self, validated_data):
        return User(**validated_data).save()
