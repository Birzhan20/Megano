from django.urls import path

from orders.views import OrdersAPIView, MyOrderAPIView


app_name = 'order'

urlpatterns = [
    path('orders', OrdersAPIView.as_view(), name='orders'),
    path('order/<int:id>', MyOrderAPIView.as_view(), name='order'),
]