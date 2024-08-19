from django.utils import timezone

from django.db import models
from goods.models import Product


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    deliveryType = models.CharField(max_length=100)
    paymentType = models.CharField(max_length=100)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


