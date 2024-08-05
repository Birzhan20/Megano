from django.urls import path, include
from rest_framework.routers import DefaultRouter
from goods.views import ProductViewSet


router = DefaultRouter()
router.register('cart', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
