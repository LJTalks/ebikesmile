from django.shortcuts import render
from .models import Product, Store


def product_list(request):
    products = Product.objects.all()
    store = Store.objects.first()  # Assumes there's only one store instance
    return render(
        request, 'store/product_list.html', {
            'products': products, 'store': store})
