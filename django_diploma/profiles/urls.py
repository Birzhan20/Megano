from django.urls import path, include
from .views import ProfileAPIView, PasswordAPIView, AvatarAPIView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('profile', ProfileViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('profile/password', PasswordAPIView.as_view(), name='password'),
    path('profile/avatar', AvatarAPIView.as_view(), name='avatar'),
]
