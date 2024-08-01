# goods/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Создайте роутер и зарегистрируйте в нем ViewSet
router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

