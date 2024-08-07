from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    fullName = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.fullName


class Avatar(models.Model):
    avatar = models.ForeignKey(Profile, related_name='avatar', on_delete=models.CASCADE)
    src = models.ImageField(blank=True)
    alt = models.CharField(max_length=120)

# {
#     "fullName": "Annoying Orange",
#     "email": "no-reply@mail.ru",
#     "phone": "88002000600",
#     "avatar": {
#         "src": "/3.png",
#         "alt": "Image alt string"
#     }
# }
