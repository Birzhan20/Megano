from django.db import models


class Payment(models.Model):
    number = models.IntegerField(max_length=16)
    name = models.CharField(max_length=128)
    month = models.IntegerField(max_length=2)
    year = models.IntegerField(max_length=2)
    code = models.IntegerField(max_length=3)
