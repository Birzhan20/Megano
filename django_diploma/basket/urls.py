from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BasketAPIView


# router = DefaultRouter()
# router.register('basket', BasketView)

urlpatterns = [
    # path('', include(router.urls)),
    path('basket', BasketAPIView.as_view(), name='basket'),
]
