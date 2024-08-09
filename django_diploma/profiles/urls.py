from django.urls import path, include
from .views import ProfileAPIView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('profile', ProfileViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]
