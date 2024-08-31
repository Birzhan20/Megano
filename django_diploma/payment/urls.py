from django.urls import path
from .views import PaymentIDAPIView, PaymentUndefinedAPIView

app_name = 'payment'

urlpatterns = [
    path('payment/undefined/', PaymentUndefinedAPIView.as_view()),

    path('api/payment/<int:id>',
         PaymentIDAPIView.as_view(),
         name='payment-online'),
]
