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


# Cannot create Sale if new Sale has same product, customer and date
def create_sale_success_view(request):
    context = {}
    if request.method == 'POST':

        product = request.POST.get('product', None)
        customer = request.POST.get('customer', None)
        date = request.POST.get('date', None)
        price = request.POST.get('price', None)
        salesperson = request.POST.get('salesperson', None)
        salespersonCommission = request.POST.get('salespersonCommission', None)


        try:

            temp = Sale.objects.get(product=product, customer=customer, date=date)

            context['error'] = 'Sale already exists'
            return render(request, 'sale/create_failure.html', context)
        except:
            sale = Sale.objects.create(product=product, customer=customer, date=date,
                                        price =price , salesperson=salesperson,
                                        salespersonCommission=salespersonCommission)


    return render(request, 'sale/create_sale_success.html', context)


def commision_report_view(request):
    sale_objects = Sale.objects.all()
    context = {
        'sale_objects': sale_objects
    }
    return render(request, 'sale/commission_report.html', context)