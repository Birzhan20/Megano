from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    fullName = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.fullName


class Avatar(models.Model):
    avatar = models.OneToOneField(Profile, related_name='avatar', on_delete=models.CASCADE)
    src = models.ImageField(blank=True)
    alt = models.CharField(max_length=120)
