from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Basket, Product
from .serializers import BasketItemSerializer


class BasketView(APIView):
    def get(self, request):
        session_key = request.session.session_key
        baskets = Basket.objects.filter(session_key=session_key)
        serializer = BasketItemSerializer(baskets, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        count = request.data.get('count')
        session_key = request.session.session_key or request.session.create()

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        basket_item, created = Basket.objects.get_or_create(
            session_key=session_key,
            product=product,
            defaults={'count': count}
        )

        if not created:
            basket_item.count += int(count)
            basket_item.save()

        serializer = BasketItemSerializer(basket_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        session_key = request.session.session_key

        try:
            basket_item = Basket.objects.get(session_key=session_key, product_id=product_id)
        except Basket.DoesNotExist:
            return Response({'error': 'Item not found in basket'}, status=status.HTTP_404_NOT_FOUND)

        basket_item.delete()
        return Response({'message': 'Item removed from basket'}, status=status.HTTP_204_NO_CONTENT)