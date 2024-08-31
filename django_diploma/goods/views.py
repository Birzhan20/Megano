from django.db.models import Avg
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Review, Product, Tag
from .serializers import ProductSerializer, ReviewSerializer, TagSerializer


class ProductAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()

    def get(self, *args, **kwargs):
        queryset = (self.queryset
                    .filter(id=kwargs['product_id'])
                    .defer("available")
                    .prefetch_related('images',
                                      'tags',
                                      'reviews',
                                      'specifications')
                    ).first()
        serializer = ProductSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewApiView(APIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()

    def get(self, *args, **kwargs) -> Response:
        review = self.queryset.filter(product_id=kwargs['product_id'])
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs) -> Response:
        request.data['product'] = kwargs['product_id']
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        average = (
            self.queryset
            .filter(product_id=kwargs['product_id'])
            .aggregate(Avg('rate'))
        )

        product = Product.objects.get(pk=kwargs['product_id'])
        product.rating = round(average['rate__avg'], 1)
        product.reviews_count += 1
        product.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class TagAPI(APIView):
    """Класс Тэг"""

    permission_classes = [AllowAny,]
    queryset = Tag.objects.all()

    def get(self, request: Request) -> Response:
        """Возвращает все тэги или тэги для конкретной категории"""

        params = request.query_params

        if params:
            queryset = self.queryset.all().filter(category=params['category'])
            serializer = TagSerializer(queryset, many=True)
        else:
            serializer = TagSerializer(self.queryset.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
