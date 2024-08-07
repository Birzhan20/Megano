from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Avatar, Profile


class SignUpSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        User.objects.create(
            user=user,
            full_name=validated_data['name'],
        )
        return user


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = 'src', 'alt'


class ProfileSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = "fullName", "email", "phone", "avatar"


