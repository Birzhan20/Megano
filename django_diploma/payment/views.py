from django.shortcuts import render
from rest_framework.views import APIView

from .models import Payment
from .serializers import PaymentSerializer


class PaymentView(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


