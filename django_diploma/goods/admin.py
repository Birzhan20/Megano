from django.contrib import admin

from .models import Product, Review, Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['description', 'price', 'count', 'title']
    list_editable = ['price', 'count']
    list_display_links = ['title']
    search_fields = ['title', 'description']
    list_filter = ['price', 'count']
    fields = [
        'category',
        'count',
        'date',
        'title',
        'tags',
        'price',
        'description',
        'full_description',
        'free_delivery',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'date', 'text']
    list_display_links = ['date']
    search_fields = ['author', 'product']
    list_filter = ['author', 'product', 'date',]
    fields = [
        'product',
        'author',
        'email',
        'text',
        'rate',
        'date',
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product']
    fields = [
        'alt',
        'product',
    ]
