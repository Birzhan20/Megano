from django.urls import path, include
from .views import SignInApiView, SignUpView, SignOutView, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('sign-in', SignInApiView.as_view(), name='sign-in'),
    path('sign-up', SignUpView.as_view(), name='sign-up'),
    path('sign-out', SignOutView.as_view(), name='sign-out'),
    path('', include(router.urls)),
]
