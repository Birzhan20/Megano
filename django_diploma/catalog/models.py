from django.db import models


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
