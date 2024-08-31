from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductAPIView, ReviewApiView, TagAPI

#app_name = 'goods'

# router = DefaultRouter()
# router.register('product', ProductViewSet,  basename='product')

urlpatterns = [
    path('product/<int:product_id>/', ProductAPIView.as_view()),
    # path('', include(router.urls)),
    path('product/<int:product_id>/reviews', ReviewApiView.as_view(), name='create-review'),
    path('tags/', TagAPI.as_view()),
    path('tags/<int:pk>', TagAPI.as_view()),
]

