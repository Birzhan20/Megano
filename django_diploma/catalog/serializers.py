from rest_framework import serializers
from goods.models import Product, Image, Tag, Review, Specifications
from .models import Category, SubCategory, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['src', 'alt']

class SubCategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'image']

class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'subcategories']







class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['src', 'alt']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = []


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'fullDescription', 'freeDelivery',
                  'images', 'tags', 'reviews', 'rating']

    def get_reviews(self, obj):
        return obj.reviews.count()