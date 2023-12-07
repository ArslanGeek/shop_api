from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ConfirmCode

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('User already exists')
        return value

class ConfirmCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmCode
        fields = ('code',)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

