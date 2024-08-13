from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Basket, Product
from .serializers import BasketSerializer


class BasketView(APIView):
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        count = request.data.get('count')
        session_key = request.session.session_key or request.session.create()

        # Проверьте, существует ли продукт
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Проверьте, есть ли уже товар в корзине
        basket_item, created = Basket.objects.get_or_create(
            session_key=session_key,
            product=product,
            defaults={'count': count}
        )

        if not created:
            # Если товар уже есть в корзине, обновите количество
            basket_item.count += int(count)
            basket_item.save()

        serializer = BasketSerializer(basket_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
