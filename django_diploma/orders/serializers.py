from rest_framework import serializers
from .models import Order
from goods.models import Product, Image, Tag


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['src', 'alt']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    tags = TagSerializer(many=True, source='tags.all')

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'price', 'count', 'date', 'title',
            'description', 'freeDelivery', 'images', 'tags', 'reviews', 'rating'
        ]


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            'id', 'createdAt', 'fullName', 'email', 'phone',
            'deliveryType', 'paymentType', 'totalCost', 'status',
            'city', 'address', 'products'
        ]
