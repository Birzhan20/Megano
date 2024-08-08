from django.utils import timezone

from rest_framework import serializers
from .models import Product, Category, Tag, Image, Review


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['src', 'alt']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'email', 'text', 'rate', 'date', 'product']
        read_only_fields = ['date', 'product']

    def create(self, validated_data):
        validated_data['date'] = timezone.now()
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.SlugRelatedField(slug_field='name', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'price', 'count', 'date', 'title',
            'description', 'fullDescription', 'freeDelivery', 'images', 'tags', 'reviews'
        ]
