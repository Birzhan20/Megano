from django.db.models import QuerySet
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from goods.models import Product
from .models import Category
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    SalesSerializer,
)
from .pagination import CustomPageNumberPagination


@method_decorator(cache_page(60*30), name='dispatch')
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60*30))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@method_decorator(cache_page(60*30), name='dispatch')
class PopularProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(popular=True)


@method_decorator(cache_page(60*30), name='dispatch')
class LimitedProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(limited=True)


@method_decorator(cache_page(60*30), name='dispatch')
class SalesProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SalesSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (AllowAny,)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(sales=True)


@method_decorator(cache_page(60*30), name='dispatch')
class BannersProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(banners=True)


@method_decorator(cache_page(60*30), name='dispatch')
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60*30))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
