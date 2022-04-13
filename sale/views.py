from django.shortcuts import render
from .models import Sale

# Create your views here.
def list_all_sales_view(request):
    sale_objects = Sale.objects.all()
    context = {
        'sale_objects': sale_objects
    }
    return render(request, 'sale/sales.html', context)

def create_sale_view(request):
    context = {}
    return render(request, 'sale/create_sale.html', context)