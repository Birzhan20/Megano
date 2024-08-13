from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BasketView


# router = DefaultRouter()
# router.register('basket', BasketView)

urlpatterns = [
    # path('', include(router.urls)),
    path('basket', BasketView.as_view(), name='basket'),
]
