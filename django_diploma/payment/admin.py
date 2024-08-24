from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    fields = ['number', 'name', 'month', 'year', 'code']
