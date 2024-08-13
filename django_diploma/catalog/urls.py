from django.urls import path
from .views import (ProductListView, CategoryListView, PopularProductView,
                    LimitedProductView, SalesProductView, BannersProductView)

urlpatterns = [
    path('catalog', ProductListView.as_view(), name='catalog'),
    path('products/popular', PopularProductView.as_view(), name='popular'),
    path('products/limited', LimitedProductView.as_view(), name='limited'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('sales', SalesProductView.as_view(), name='sale'),
    path('banners', BannersProductView.as_view(), name='banners'),
]
