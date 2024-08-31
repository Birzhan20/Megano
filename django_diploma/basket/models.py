from django.db import models
from django.utils import timezone

from goods.format_date import format_date
from goods.models import Product
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Basket(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="имя пользоваткля")

    product = models.ForeignKey(Product,
                                related_name='items',
                                on_delete=models.CASCADE,
                                verbose_name='товар')

    count = models.PositiveIntegerField(null=True,
                                        default=None,
                                        verbose_name='количество', )

    date = models.CharField(default=format_date(datetime.now()),
                            max_length=100)

    order = models.PositiveIntegerField(null=True,
                                        default=None,
                                        verbose_name='номер заказа', )

    class Meta:
        verbose_name = 'Товар_в_корзине_пользователя'
        verbose_name_plural = 'Товары в корзинах пользователей'
        ordering = ['id', ]

    def __str__(self) -> str:
        """Заголовок страницы описания товара."""

        return (f"Товар_в_корзине_пользователя: (id объекта = {self.id},"
                f"\nимя пользователя: {self.user})")
