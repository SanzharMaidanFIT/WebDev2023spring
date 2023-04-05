from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, Category
from django.forms.models import model_to_dict

def products(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    return JsonResponse(data)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    data = {"product": model_to_dict(product)}
    return JsonResponse(data)

def categories(request):
    categories = Category.objects.all()
    data = {"categories": list(categories.values())}
    return JsonResponse(data)

def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    data = {"category": model_to_dict(category)}
    return JsonResponse(data)

def category_products(request, id):
    category = get_object_or_404(Category, pk=id)
    products = Product.objects.filter(category=category)
    data = {"products": list(products.values())}
    return JsonResponse(data)

