import os
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.utils import json

from django_diploma import settings
from profiles.models import Profile
from orders.models import Order
from orders.serializers import MyOrderSerializer, OrderSerializer
from .path import directory_path


class OrdersAPIView(APIView):
    def get(self, request: Request) -> Response:
        queryset = Order.objects.filter(user_id=request.user.id)
        orders = []
        orders_ids = [order.id for order in queryset]

        if not orders_ids:
            return Response("No orders found for this user.", status=404)

        missing_files = []

        for order_id in orders_ids:
            file_path = os.path.join(
                settings.BASE_DIR,
                f"media/orders_full/user{request.user.id}_order{order_id}.json"
            )

            try:
                with open(file_path, 'r') as file:
                    order_data = json.load(file)
                    orders.append(order_data)
            except FileNotFoundError:
                missing_files.append(order_id)
                return Response(
                    {
                        "error":
                            "Order file for order ID %d not found" % order_id},
                    status=404
                )

        if missing_files:
            return Response(
                {
                    "error":
                        "Order files not found for order IDs: %s" % ', '.join(
                            map(str, missing_files)
                        )
                },
                status=404
            )

        return Response(orders, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs) -> Response:
        Order.objects.create(user_id=request.user.id)
        last_order = Order.objects.filter(user_id=request.user.id).last()
        with open(directory_path('order_products',
                                 request.user.id, last_order.id), 'w') as file:
            json.dump(request.data, file, indent=2)
        profile = Profile.objects.get(user_id=request.user.id)

        serializer = MyOrderSerializer(data={'user': request.user.id,
                                             'fullName': profile.fullName,
                                             'phone': profile.phone,
                                             'email': profile.email,
                                             'deliveryType': 'ordinary',
                                             'paymentType': 'online'},
                                       context={'file_name': file.name},
                                       instance=last_order,)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            last_order.delete()

        return Response({"orderId": last_order.id},
                        status=status.HTTP_201_CREATED)


class MyOrderAPIView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        queryset = Order.objects.get(id=kwargs['id'])
        serializer = OrderSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs) -> Response:
        def delivery_cost():
            final_cost = 0
            if request.data["basketCount"]["price"] < 2000:
                final_cost += 200
            if request.data["deliveryType"] == "express":
                final_cost += 500

            return final_cost

        request.data["totalCost"] = (
                request.data["basketCount"]["price"] + delivery_cost()
        )
        request.data["id"] = request.data.pop("orderId")

        with open(directory_path('orders_full',
                                 request.user.id, kwargs['id']), 'w') as file:
            json.dump(request.data, file, indent=2)

        instance = Order.objects.get(id=kwargs['id'])
        serializer = OrderSerializer(
            data={'deliveryType': request.data["deliveryType"],
                  "paymentType": request.data["paymentType"],
                  "totalCost": round(request.data["totalCost"], 1),
                  "city": request.data["city"],
                  "address": request.data["address"],
                  "status": request.data["status"]},
            instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
