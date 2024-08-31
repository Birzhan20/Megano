from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from basket.models import Basket
from basket.serializers import BasketSerializer, ItemInBasketSerializer
from goods.models import Product


class BasketAPIView(APIView):
    permission_classes = (AllowAny,)
    queryset = Basket.objects.all()

    def get(self, request: Request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/sign-in')
        items = (self.queryset
                 .order_by('product_id')
                 .filter(user_id=request.user.id)
                 .select_related('product'))

        products_id = [item.product.id for item in items]

        products = (Product.objects
                    .order_by('id')
                    .filter(pk__in=products_id)
                    .prefetch_related('tags', 'reviews', 'images'))
        context = [item.count for item in items]

        if products.exists():
            serializer = BasketSerializer(products, many=True, context={
                'context': context})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK)

    def post(self, request: Request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/sign-in',)
        try:
            item = (self.queryset.get(
                user_id=request.user.id,
                product_id=request.data["id"])
            )
            item.count += request.data["count"]
            item.save()
            answer = self.get(request=request)
            return answer

        except Basket.DoesNotExist:
            data = {'user_id': request.user.id,
                    'product': Product.objects.get(id=request.data['id']),
                    'count': request.data['count']}
            serializer = ItemInBasketSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(data='successful operation',
                            status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        item = (self.queryset.get(
            user_id=request.user.id,
            product_id=request.data["id"])
        )
        if item.count == request.data["count"]:
            item.delete()
        else:
            item.count -= request.data["count"]
            item.save()

        return_to_basket = self.get(request=request)
        return return_to_basket
