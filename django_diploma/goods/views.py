from datetime import datetime

from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        # Добавляем product_id в данные запроса
        data = request.data.copy()
        data['product'] = product_id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                reviews = Review.objects.filter(product=product)
                reviews_serializer = ReviewSerializer(reviews, many=True)
                return Response(reviews_serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                # Логирование ошибки
                print(f"Ошибка при сохранении отзыва: {e}")
                return Response({"error": "Ошибка при сохранении отзыва"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
