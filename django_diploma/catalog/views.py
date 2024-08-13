from rest_framework import generics
from goods.models import Product
from .serializers import ProductSerializer, CategorySerializer, SaleProductSerializer, SaleImageSerializer
from .pagination import CustomPageNumberPagination
from .models import Category, SaleProduct, SaleImage


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination


class PopularProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(popular=True)


class LimitedProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(limited=True)


class SalesProductView(generics.ListAPIView):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer
    pagination_class = CustomPageNumberPagination


class BannersProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(banners=True)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

