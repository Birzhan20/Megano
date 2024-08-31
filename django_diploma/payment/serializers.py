from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['number', 'name', 'month', 'year', 'code', 'order']

    def validate(self, attrs):
        month = attrs.get('month')

        if (int(month) < 1) or (int(month) > 12):
            raise serializers.ValidationError(
                '"month" must be between 1 and 12 inclusive')
        return attrs


