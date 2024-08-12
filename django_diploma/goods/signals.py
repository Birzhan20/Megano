from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review


@receiver(post_save, sender=Review)
def update_product_rating(sender, instance, **kwargs):
    product = instance.product
    product.rating = product.calculate_rating()
    product.save()
