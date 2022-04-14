from django.shortcuts import render
from .models import Product

# Create your views here.
def list_all_products_view(request):
    product_objects = Product.objects.all()
    context = {
        'product_objects': product_objects
    }
    return render(request, 'inventory/products.html', context)

def edit_product_view(request, id):
    product_objects = Product.objects.get(pk=id)
    context = {
        'product_objects': product_objects
    }
    return render(request, 'inventory/edit_product.html', context)

def edit_success_view(request, id):
    context = {}
    return render(request, 'inventory/edit_success.html', context)

def add_product_view(request):
    context = {}
    return render(request, 'inventory/create_product.html', context)

def add_product_success_view(request):
    #
    #
    return render(request, 'inventory/add_success.html', context)