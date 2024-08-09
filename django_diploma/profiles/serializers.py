from rest_framework import serializers
from .models import Avatar, Profile


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['src', 'alt']


class ProfileSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(read_only=True)  # Используйте read_only=True, если не требуется записывать данные

    class Meta:
        model = Profile
        fields = ['fullName', 'email', 'phone', 'avatar']
