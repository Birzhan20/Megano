from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['createdAt', 'fullName']
    list_display_links = ['fullName']
    fields = ['fullName', 'email', 'phone', 'deliveryType', 'paymentType', 'totalCost',
              'status', 'city', 'address', 'products']
