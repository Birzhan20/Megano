from django.contrib import admin

from .models import Product, Review, Image, Specifications, Tag



@admin.register(Tag)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name']
    fields = ['name', 'product', 'category']


@admin.register(Specifications)
class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name']
    fields = ['name', 'value', 'product']


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
        'price',
        'description',
        'fullDescription',
        'freeDelivery',
        'popular',
        'limited',
        'sales',
        'banners',
        'subcategory',
        'dateFrom',
        'dateTo',
        'salePrice'
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
    list_display = ['product_title']
    fields = [
        'alt',
        'product',
        'src',
    ]

    def product_title(self, obj):
        return obj.product.title

    product_title.short_description = 'Product Title'
