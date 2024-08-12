from django.utils import timezone

from rest_framework import serializers
from .models import Product, Category, Tag, Image, Review, Specifications


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'name'


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = ['name', 'value']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['src', 'alt']


class ReviewSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=False, read_only=True)

    class Meta:
        model = Review
        fields = ['author', 'email', 'text', 'rate', 'date']

    def create(self, validated_data):
        product = self.context.get('product')
        return Review.objects.create(product=product, **validated_data)


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.SlugRelatedField(slug_field='name', queryset=Tag.objects.all(), many=True)
    specifications = SpecificationsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'price', 'count', 'date', 'title',
            'description', 'fullDescription', 'freeDelivery',
            'images', 'tags', 'reviews', 'specifications', 'rating'
        ]
