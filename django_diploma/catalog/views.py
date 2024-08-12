from rest_framework import generics
from goods.models import Product
from .serializers import ProductSerializer, CategorySerializer
from .pagination import CustomPageNumberPagination
from .models import Category


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

