from rest_framework import serializers

from .models import Review, Product, Specifications, Image, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name',]


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['author', 'email', 'text', 'rate', 'date', 'product']

    def to_representation(self, instance):
        data = super(ReviewSerializer, self).to_representation(instance)
        data.pop('product')
        return data


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = ['value', 'name']


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = [
            'src',
            'alt',
        ]


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    specifications = SpecificationSerializer(many=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "fullDescription",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "specifications",
            "rating",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tags'] = [item['name'] for item in data['tags']]
        if not data['images']:
            data['images'] = [{'alt': 'no image'}]
        return data
