from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from orders.models import Order


class Payment(models.Model):

    number = models.IntegerField(
        validators=[
            MaxValueValidator(9999999999999999),
            MinValueValidator(0)
        ]
    )

    name = models.CharField(max_length=128)

    month = models.IntegerField(
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0)
        ]
    )

    year = models.IntegerField(
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0)
        ]
    )

    code = models.IntegerField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(0)
        ]
    )

    order = models.OneToOneField(Order, on_delete=models.PROTECT)
