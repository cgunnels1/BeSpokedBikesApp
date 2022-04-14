from django.shortcuts import render
from .models import Discount

# Create your views here.
def list_all_discounts_view(request):
    discount_objects = Discount.objects.all()
    context = {
        'discount_objects': discount_objects
    }
    return render(request, 'discounts/discounts.html', context)