from django.urls import path
from .views import SignInApiView

urlpatterns = [
    path('sign-in', SignInApiView.as_view(), name='sign-in'),
]
