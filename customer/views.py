from django.shortcuts import render
from .models import Customer


# Create your views here.
def index_view(request):
    context = {}
    return render(request, 'client/index.html', context)


def list_all_customers_view(request):
    customer_objects = Customer.objects.all()
    context = {
        'customer_objects': customer_objects
    }
    return render(request, 'client/customers.html', context)
