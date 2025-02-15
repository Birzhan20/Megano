# Generated by Django 4.2.7 on 2024-08-28 18:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import goods.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_index=True, primary_key=True, serialize=False
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        db_index=True,
                        decimal_places=2,
                        default=0,
                        max_digits=8,
                        verbose_name="цена",
                    ),
                ),
                (
                    "sale",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="распродажа"
                    ),
                ),
                (
                    "salePrice",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=8,
                        verbose_name="цена со скидкой",
                    ),
                ),
                (
                    "dateFrom",
                    models.DateField(
                        blank=True, null=True, verbose_name="начало скидки"
                    ),
                ),
                (
                    "dateTo",
                    models.DateField(
                        blank=True, null=True, verbose_name="окончание скидки"
                    ),
                ),
                ("count", models.IntegerField(default=0, verbose_name="количество")),
                (
                    "date",
                    models.CharField(
                        default="Wed Aug 28 2024 21:19:39 GMT+0300 (Europe/Moscow)",
                        max_length=100,
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="название")),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="краткое описание"),
                ),
                (
                    "fullDescription",
                    models.TextField(
                        blank=True, db_index=True, verbose_name="полное описание"
                    ),
                ),
                (
                    "freeDelivery",
                    models.BooleanField(
                        default=False, verbose_name="бесплатная доставка"
                    ),
                ),
                (
                    "rating",
                    models.DecimalField(
                        db_index=True,
                        decimal_places=1,
                        default=0,
                        max_digits=3,
                        verbose_name="рейтинг",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="в наличии"),
                ),
                (
                    "limited",
                    models.BooleanField(default=False, verbose_name="тираж ограничен"),
                ),
                (
                    "reviews_count",
                    models.IntegerField(default=0, verbose_name="отзывов"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="ID категории",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.subcategory",
                        verbose_name="ID подкатегории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["id", "title"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="название"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="категория",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags",
                        to="goods.product",
                        verbose_name="товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Specifications",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=250, verbose_name="характеристика"),
                ),
                ("value", models.CharField(max_length=250, verbose_name="значение")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specifications",
                        to="goods.product",
                        verbose_name="товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Характеристика",
                "verbose_name_plural": "Характеристики",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=100, verbose_name="автор")),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("text", models.TextField(max_length=2000)),
                (
                    "rate",
                    models.PositiveIntegerField(
                        default=5,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="оценка",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="goods.product",
                        verbose_name="товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_index=True, primary_key=True, serialize=False
                    ),
                ),
                (
                    "src",
                    models.ImageField(
                        blank=True,
                        default=None,
                        upload_to=goods.models.product_images_directory_path,
                        verbose_name="адрес",
                    ),
                ),
                (
                    "alt",
                    models.CharField(
                        blank=True,
                        default="image_description",
                        max_length=200,
                        verbose_name="описание",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="goods.product",
                        verbose_name="товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Картинка товара",
                "verbose_name_plural": "Картинки товаров",
                "ordering": ["id"],
            },
        ),
    ]
