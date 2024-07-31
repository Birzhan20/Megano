from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from django.shortcuts import render


class ProductDetailAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return render(request, 'frontend/product.html', {'product': None})

        serializer = ProductSerializer(product)
        return render(request, 'frontend/product.html', {'product': serializer.data})


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
