from django.utils import timezone

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    fullDescription = models.TextField()
    freeDelivery = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    src = models.ImageField(blank=False)
    alt = models.CharField(max_length=255)


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    rate = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)


# class Specifications(models.Model):
#     name = models.CharField()
#     value = models.CharField()