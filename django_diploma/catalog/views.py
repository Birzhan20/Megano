from rest_framework import generics
from goods.models import Product
from .serializers import ProductSerializer, CategorySerializer, SaleProductSerializer, SaleImageSerializer
from .pagination import CustomPageNumberPagination
from .models import Category, SaleProduct, SaleImage
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60*30), name='dispatch')
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination


@method_decorator(cache_page(60*30), name='dispatch')
class PopularProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(popular=True)


@method_decorator(cache_page(60*30), name='dispatch')
class LimitedProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(limited=True)


@method_decorator(cache_page(60*30), name='dispatch')
class SalesProductView(generics.ListAPIView):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer
    pagination_class = CustomPageNumberPagination


@method_decorator(cache_page(60*30), name='dispatch')
class BannersProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(banners=True)


@method_decorator(cache_page(60*30), name='dispatch')
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

