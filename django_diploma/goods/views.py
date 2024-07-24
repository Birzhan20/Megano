from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product


class ProductTemplateView(TemplateView):
    template_name = 'frontend/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs.get('id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            product = None
        context['product'] = product
        return context

