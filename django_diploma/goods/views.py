from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.renderers import TemplateHTMLRenderer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer
# from .models import Product
#
# class ProductHTMLView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'frontend/product.html'
#
#     def get(self, request, id, *args, **kwargs):
#         try:
#             product = Product.objects.get(id=id)
#             return Response({'product': product})
#         except Product.DoesNotExist:
#             return Response({'error': 'Product not found'}, status=404)


