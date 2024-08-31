from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from catalog.models import Category, SubCategory
from .format_date import format_date


class Product(models.Model):
    """
        Модель 'Product' представляет собой
        базовую модель товара.

        Заказы тут: :model:`order.Order`

        Attributes:
            id (obj): уникальный номер товара
            category (obj): категория товара
            subcategory (obj): подкатегория товара
            price (obj): цена товара
            sale (obj): участвует ли товар в распродаже
            salePrice (obj): цена товара для распродажи
            dateFrom (obj): дата начала распродажи
            dateTo (obj): дата завершения распродажи
            count (obj): количество единиц товара в наличии
            title (obj): название товара
            description (obj): краткое описание товара
            fullDescription (obj): полное описание товара
            freeDelivery (obj): бесплатная доставка
            rating (obj): рейтинг товара
            sort_index (obj): индекс сортировки товара
            purchases (obj): продано единиц товара
            reviews_count (obj): количество отзывов на товар

        """

    id = models.IntegerField(db_index=True, primary_key=True)

    category = models.ForeignKey(Category,
                                 blank=False,
                                 null=False,
                                 default=None,
                                 on_delete=models.CASCADE,
                                 verbose_name='ID категории')

    subcategory = models.ForeignKey(SubCategory,
                                    blank=False,
                                    null=False,
                                    on_delete=models.CASCADE,
                                    verbose_name='ID подкатегории')

    price = models.DecimalField(default=0,
                                max_digits=8,
                                decimal_places=2,
                                db_index=True,
                                verbose_name='цена',)

    sale = models.BooleanField(default=False,
                               db_index=True,
                               verbose_name='распродажа')

    salePrice = models.DecimalField(default=0,
                                    blank=True,
                                    max_digits=8,
                                    decimal_places=2,
                                    verbose_name='цена со скидкой', )

    dateFrom = models.DateField(null=True,
                                blank=True,
                                verbose_name='начало скидки',)

    dateTo = models.DateField(null=True,
                              blank=True,
                              verbose_name='окончание скидки',)

    count = models.IntegerField(default=0, verbose_name='количество')

    date = models.CharField(default=format_date(datetime.now()),
                            max_length=100)

    title = models.CharField(max_length=100, verbose_name='название')

    description = models.CharField(max_length=100,
                                   verbose_name='краткое описание')

    fullDescription = models.TextField(null=False,
                                       blank=True,
                                       db_index=True,
                                       verbose_name='полное описание')

    freeDelivery = models.BooleanField(default=False,
                                       verbose_name='бесплатная доставка')

    rating = models.DecimalField(default=0,
                                 max_digits=3,
                                 decimal_places=1,
                                 db_index=True,
                                 verbose_name='рейтинг')

    available = models.BooleanField(null=False,
                                    default=True,
                                    verbose_name='в наличии')

    limited = models.BooleanField(default=False,
                                  verbose_name='тираж ограничен')

    reviews_count = models.IntegerField(default=0,
                                        verbose_name='отзывов')

    popular = models.BooleanField(default=False)

    limited = models.BooleanField(default=False)

    sales = models.BooleanField(default=False)

    banners = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id', 'title']

    def __str__(self) -> str:
        """Заголовок страницы описания товара."""

        return f"Товар (id = {self.id}, название = {self.title!r})"


def product_images_directory_path(instance: "Product", filename: str) -> str:
    """Функция генерации пути хранения аватарок изображения товара"""

    return "products_images/product_{id}/{filename}".format(
        id=instance.product_id,
        filename=filename,
    )


class Image(models.Model):
    """Product image"""

    id = models.IntegerField(db_index=True, primary_key=True)

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images",
                                verbose_name="товар",)

    src = models.ImageField(default=None,
                            blank=True,
                            upload_to=product_images_directory_path,
                            verbose_name='адрес',)

    alt = models.CharField(default='image_description',
                           max_length=200,
                           blank=True,
                           verbose_name='описание',)

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товаров'
        ordering = ['id', ]


    def __str__(self) -> str:
        """Заголовок страницы описания характеристики товара."""

        return (f"Картинка товара (id = {self.id}, "
                f"описание = {self.alt!r})")


@receiver(pre_delete, sender=Image)
def image_model_delete(sender, instance, **kwargs):
    if instance.src:
        instance.src.delete(False)


class Review(models.Model):
    """Product review model"""

    author = models.CharField(max_length=100,
                              null=False,
                              blank=False,
                              verbose_name='автор',)

    email = models.EmailField(null=True, blank=True)

    text = models.TextField(max_length=2000, null=False, blank=False)

    rate = models.PositiveIntegerField(default=5,
                                       null=False,
                                       blank=False,
                                       validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)],
                                       verbose_name='оценка',)

    date = models.DateTimeField(default=datetime.now, verbose_name='дата')

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name='товар',
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id',]

    def __str__(self) -> str:
        """Заголовок страницы описания характеристики товара."""

        return (f"Отзыв (id = {self.id}, "
                f"оценка = {self.rate!r}, автор = {self.author!r})")


class Specifications(models.Model):
    """Product specification"""

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="specifications",
                                verbose_name="товар")

    name = models.CharField(max_length=250,
                            null=False,
                            blank=False,
                            verbose_name="характеристика")

    value = models.CharField(max_length=250,
                             null=False,
                             blank=False,
                             verbose_name="значение")

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'
        ordering = ['id',]

    def __str__(self) -> str:
        """Заголовок страницы описания характеристики товара."""

        return f"Характеристика (id = {self.id}, название = {self.name!r})"


class Tag(models.Model):
    """
    Модель 'Tag' представляет собой тэг товара.

    Attributes:
        name (obj): название тэга
        category (obj): категория товара
        product (obj): ID товара
    """

    name = models.CharField(max_length=100,
                            unique=False,
                            verbose_name='название')

    category = models.ForeignKey(Category,
                                 blank=True,
                                 null=True,  # Позволяет быть пустым в базе данных
                                 on_delete=models.CASCADE,
                                 verbose_name='категория',)

    product = models.ManyToManyField(Product,
                                related_name='tags',
                                verbose_name='товар',)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['id']

    def __str__(self) -> str:
        """Заголовок страницы описания тэга."""
        return f"Тэг (id = {self.id}, название = {self.name!r})"
