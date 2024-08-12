from django.urls import path
from .views import ProductListView, CategoryListView

urlpatterns = [
    path('catalog', ProductListView.as_view(), name='catalog'),
    # path('products/popular', .as_view(), name='popular'),
    # path('products/limited', .as_view(), name='limited'),
    path('categories', CategoryListView.as_view(), name='limited'),
    # path('sale', .as_view(), name='limited'),
    # path('banners', .as_view(), name='limited'),
]
