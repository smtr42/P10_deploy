from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from products.models import Product


def complete(request):
    searched_term = request.GET.get("term")
    products = get_object_or_404(
        Product.objects.get_all_by_term(searched_term))
    products = [product.product_name for product in products]
    return JsonResponse(products, safe=False)
