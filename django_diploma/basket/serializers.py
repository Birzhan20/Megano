from rest_framework import serializers

from goods.models import Product
from .models import Basket
from goods.serializers import (ReviewSerializer,
                                 ProductImageSerializer,
                                 ProductSerializer,
                               TagSerializer)


class BasketSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True)
    i = 0

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "rating",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["count"] = self.context['context'][self.i]
        data["reviews"] = len(data["reviews"])
        self.i += 1
        return data


class ItemInBasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Basket
        fields = [
            'product',
            'count',
        ]

    def to_internal_value(self, data):
        return data
