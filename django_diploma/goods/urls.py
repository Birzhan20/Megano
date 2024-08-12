from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CreateReviewView, TagsView


router = DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product/<int:product_id>/reviews', CreateReviewView.as_view(), name='create-review'),
    path('tags', TagsView.as_view(), name='tags'),
]

