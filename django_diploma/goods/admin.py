from django.contrib import admin

from .models import Product, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity']
    list_editable = ['price', 'quantity']
    list_display_links = ['name']
    search_fields = ['name', 'description']
    list_filter = ['name', 'price', 'quantity']
    fields = [
        'name',
        'image',
        'price',
        'quantity',
        'description',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'created_at', 'comment']
    list_display_links = ['created_at']
    search_fields = ['author', 'product']
    list_filter = ['author', 'product', 'created_at',]
