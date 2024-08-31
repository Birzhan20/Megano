import json
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.serializers import PaymentSerializer
from orders.models import Order
from orders.path import directory_path
from .verification import payment_verification


class PaymentUndefinedAPIView(APIView):
    def get(self, request: Request) -> HttpResponseRedirect:
        queryset = Order.objects.all().last()

        if queryset.paymentType == 'online':
            return HttpResponseRedirect(f'/payment/{queryset.id}')


class PaymentIDAPIView(APIView):
    def payment_processing(self, number: str):
        try:
            payment_result = payment_verification(number)
            return payment_result
        except Exception as e:
            print(f'Произошла ошибка: {e}')
            return f"Произошла ошибка: {e}"

    def post(self, request: Request, *args, **kwargs):
        request.data['order'] = kwargs['id']
        number = request.data['number']
        payment_result = self.payment_processing(number)

        if payment_result == 'successful operation':
            serializer = PaymentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            Order.objects.filter(id=kwargs['id']).update(status='paid')
            path_to_file = directory_path(
                'orders_full', request.user.id, kwargs['id'])

            with open(path_to_file, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                data["status"] = "paid"
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=2)
                file.truncate()

            print("Статус успешно обновлён на 'paid'.")

            return Response(data=payment_result,
                            status=status.HTTP_200_OK)

        return Response(data=payment_result,
                        status=status.HTTP_402_PAYMENT_REQUIRED)
