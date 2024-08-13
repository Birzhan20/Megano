from django.db import models


class SaleProduct(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salePrice = models.DecimalField(max_digits=10, decimal_places=2)
    dateFrom = models.DateField()
    dateTo = models.DateField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SaleImage(models.Model):
    product = models.ForeignKey(SaleProduct, related_name='images', on_delete=models.CASCADE)
    src = models.ImageField(blank=False)
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.product.title


class Image(models.Model):
    src = models.ImageField(blank=False)
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.alt


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.OneToOneField(Image, related_name='category_image', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    image = models.OneToOneField(Image, related_name='subcategory_image', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
