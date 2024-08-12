from django.utils import timezone

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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
    rating = models.FloatField(default=0.0)

    def calculate_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total_rating = sum(review.rate for review in reviews)
            average_rating = total_rating / reviews.count()
            return average_rating
        return 0.0


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    src = models.ImageField(blank=False)
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.product.title


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    rate = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)


class Specifications(models.Model):
    product = models.ForeignKey(Product, related_name='specifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name
