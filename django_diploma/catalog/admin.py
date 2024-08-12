from django.contrib import admin
from catalog.models import Category, SubCategory, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_display_links = ['title']
    fields = ['title', 'image']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image']
    list_display_links = ['title']
    fields = ['title', 'category', 'image']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['src', 'alt']
    list_display_links = ['src']
    fields = ['src', 'alt']

