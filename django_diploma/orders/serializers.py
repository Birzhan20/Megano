from rest_framework import serializers
from .models import Order, Product, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'freeDelivery', 'images', 'tags', 'reviews', 'rating']


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ['product', 'count']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)  # Связь с продуктами через OrderProduct

    class Meta:
        model = Order
        fields = ['id', 'createdAt', 'fullName', 'email', 'phone', 'deliveryType', 'paymentType', 'totalCost', 'status', 'city', 'address', 'products']
