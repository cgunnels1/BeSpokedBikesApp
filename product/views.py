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
    product = Product.objects.get(pk=id)
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', None)
        manufacturer = request.POST.get('manufacturer', None)
        style = request.POST.get('style', None)
        purchase_price = request.POST.get('purchase_price', None)
        sale_price = request.POST.get('sale_price', None)
        quantity_on_hand = request.POST.get('quantity_on_hand', None)
        commission_percentage = request.POST.get('commission_percentage', None)

        product_query = Product.objects.filter(name=name)

        if (product.name == name):
            if str(product.sale_price) != str(sale_price) or str(product.quantity_on_hand) != str(
                    quantity_on_hand) or str(product.commission_percentage) != str(commission_percentage):
                print()
            else:
                context['error'] = 'Product already exists'
                return render(request, 'inventory/edit_failure.html', context)
        elif product_query.exists():

            context['error'] = 'Product already exists'
            return render(request, 'inventory/edit_failure.html', context)

        product.name = name
        product.manufacturer = manufacturer
        product.style = style
        product.purchase_price = purchase_price
        product.sale_price = sale_price
        product.quantity_on_hand = quantity_on_hand
        product.commission_percentage = commission_percentage
        product.save()

    return render(request, 'inventory/edit_success.html', context)


def add_product_view(request):
    context = {}
    return render(request, 'inventory/create_product.html', context)


# Cannot add new product if new product has the same name as pre-existing product
def add_product_success_view(request):
    context = {}
    if request.method == 'POST':

        name = request.POST.get('name', None)
        manufacturer = request.POST.get('manufacturer', None)
        style = request.POST.get('style', None)
        purchase_price = request.POST.get('purchase_price', None)
        sale_price = request.POST.get('sale_price', None)
        quantity_on_hand = request.POST.get('quantity_on_hand', None)
        commission_percentage = request.POST.get('commission_percentage', None)

        try:

            temp = Product.objects.get(name=name, manufacturer=manufacturer, style=style)

            context['error'] = 'Product already exists'
            return render(request, 'inventory/edit_failure.html', context)
        except:
            product = Product.objects.create(name=name, manufacturer=manufacturer, style=style,
                                             purchase_price=purchase_price, sale_price=sale_price,
                                             quantity_on_hand=quantity_on_hand,
                                             commission_percentage=commission_percentage)

    return render(request, 'inventory/add_success.html', context)
