from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Basket, Product
from .serializers import BasketItemSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class BasketView(APIView):
    @method_decorator(cache_page(60 * 1), name='dispatch')
    def get(self, request):
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        basket_items = Basket.objects.filter(session_key=session_key).select_related('product')
        if not basket_items.exists():
            return Response({'error': 'Basket is empty'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BasketItemSerializer(basket_items, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        count = request.data.get('count')

        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

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

        basket_items = Basket.objects.filter(session_key=session_key).select_related('product')
        serializer = BasketItemSerializer(basket_items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        session_key = request.session.session_key

        if not session_key:
            return Response({'error': 'Session key is missing'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            basket_item = Basket.objects.get(session_key=session_key, product_id=product_id)
        except Basket.DoesNotExist:
            return Response({'error': 'Item not found in basket'}, status=status.HTTP_404_NOT_FOUND)

        basket_item.delete()

        basket_items = Basket.objects.filter(session_key=session_key).select_related('product')
        if not basket_items.exists():
            return Response([], status=status.HTTP_204_NO_CONTENT)

        serializer = BasketItemSerializer(basket_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
