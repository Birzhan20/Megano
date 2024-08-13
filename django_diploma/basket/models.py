from django.db import models
from django.utils import timezone
from goods.models import Product

class Basket(models.Model):
    session_key = models.CharField(max_length=255, default='default_session_key')  # Идентификатор сессии пользователя
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Ссылка на продукт
    count = models.PositiveIntegerField()  # Количество товара
    date_added = models.DateTimeField(default=timezone.now)  # Дата добавления в корзину

    class Meta:
        unique_together = ('session_key', 'product')  # Уникальность корзины по сессии и продукту

    def __str__(self):
        return f"{self.product.title} in basket for session {self.session_key}"
