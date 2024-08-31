from django.db import models
from goods.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        null=True
    )

    createdAt = models.DateTimeField(
        auto_now=True,
        verbose_name='дата'
    )

    fullName = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default='anonymous',
        verbose_name='полное имя заказчика'
    )

    email = models.EmailField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='почта'
    )

    phone = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='телефон'
    )

    deliveryType = models.CharField(
        blank=False,
        max_length=20,
        db_index=True,
        verbose_name='тип доставки',
        choices=(
            ('ordinary', 'Доставка'),
            ('express', 'Экспресс-доставка'),
        )
    )

    paymentType = models.CharField(
        blank=False,
        max_length=40,
        db_index=True,
        verbose_name='тип оплаты',
        choices=(
            ('online', 'Онлайн картой'),
            ('someone', 'Онлайн со случайного чужого счёта'),
        )
    )

    totalCost = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        null=True,
        verbose_name='полная стоимость'
    )

    status = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='статус',
        choices=(
            ('in processing', 'В обработке'),
            ('paid', 'Оплачено')
        )
    )

    city = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        verbose_name='город'
    )

    address = models.CharField(
        max_length=400,
        blank=False,
        null=True,
        verbose_name='адрес'
    )

    products = models.FileField(default=None)

    order_name = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        unique=True,
        verbose_name='Название заказа'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['id']

    def __str__(self) -> str:
        """Заголовок страницы описания заказа."""
        return f"Заказ (id = {self.id}; статус = {self.status!r})"
