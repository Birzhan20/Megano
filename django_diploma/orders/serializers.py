from rest_framework import serializers
from rest_framework.utils import json

from profiles.serializers import ProfileSerializer
from orders.models import Order
from goods.format_date import format_date
from .path import directory_path


class MyOrderSerializer(serializers.ModelSerializer):
    fullName = ProfileSerializer

    class Meta:
        model = Order
        fields = ['user', 'fullName', 'phone', 'email', 'address',
                  'city', 'deliveryType', 'paymentType']

    def to_internal_value(self, data):
        return data

    def update(self, instance, validated_data):
        instance.fullName = validated_data['fullName']
        instance.phone = validated_data['phone']
        instance.email = validated_data['email']
        instance.status = 'in processing'
        instance.deliveryType = validated_data['deliveryType']
        instance.paymentType = validated_data['paymentType']
        instance.products = self.context['file_name']
        instance.order_name = self.context['file_name']
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField(required=False)

    @staticmethod
    def get_createdAt(obj):
        createdAt = format_date(obj.createdAt, month='digit')
        return createdAt

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        with open(directory_path('order_products',
                                 instance.user_id, instance.id), 'r') as file:
            data['products'] = json.load(file)

            return data
