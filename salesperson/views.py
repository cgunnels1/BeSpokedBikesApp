from django.shortcuts import render
from .models import Salesperson

# Create your views here.
def salesperson_all_staff_view(request):
    salesperson_objects = Salesperson.objects.all()
    context = {
        'salesperson_objects': salesperson_objects
    }
    return render(request, 'directory/staff_directory.html', context)

def edit_salesperson_view(request):
    context = {}
    return render(request, 'directory/edit_salesperson.html', context)

def salesperson_commision_report_view(request):
    context = {}
    return render(request, 'directory/commission_report.html', context)