from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory

def product_list(request):
    products = Product.objects.filter()
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
    context = {
        'product': product,
        'related' : related_products
    }
    return render(request, 'products/product_detail.html', context)
