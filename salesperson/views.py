from django.shortcuts import render
from .models import Salesperson



# Create your views here.
def salesperson_all_staff_view(request):
    salesperson_objects = Salesperson.objects.all()
    context = {
        'salesperson_objects': salesperson_objects
    }
    return render(request, 'directory/staff_directory.html', context)

def edit_salesperson_view(request, id):
    salesperson_objects = Salesperson.objects.get(pk=id)
    context = {
        'salesperson_objects': salesperson_objects
    }
    return render(request, 'directory/edit_salesperson.html', context)

def edit_success_view(request, id):
    salesperson = Salesperson.objects.get(pk=id)

    context = {}
    if request.method == 'POST':
        fname = request.POST.get('fname', None)
        lname = request.POST.get('lname', None)
        address = request.POST.get('address', None)
        phoneNumber = request.POST.get('phonenumber', None)
        startdate = request.POST.get('startdate', None)
        terminationDate = request.POST.get('terminationdate')
        manager = request.POST.get('manager', None)

        person_query = Salesperson.objects.filter(firstName=fname, lastName=lname, startDate=startdate)


        if (salesperson.firstName == fname and salesperson.lastName == lname and str(salesperson.startDate) == str(startdate)):

            context['error'] = 'Salesperson already exists'
            return render(request, 'directory/edit_failure.html', context)
        elif person_query.exists():
            #print("Query does exist")
            context['error'] = 'Salesperson already exists'
            return render(request, 'directory/edit_failure.html', context)
        else:
            salesperson.firstName = fname
            salesperson.lastName = lname
            salesperson.address = address
            salesperson.phoneNumber = phoneNumber
            salesperson.startDate = startdate
            salesperson.terminationDate = terminationDate
            salesperson.manager = manager
            salesperson.save()

    return render(request, 'directory/edit_success.html', context)

def add_salesperson_view(request):
    # salesperson = Salesperson.objects.get(pk=id)
    context = {}
    return render(request, 'directory/create_salesperson.html', context)

#Cannot create new salesperson if firstName, lastName and startDate are the same as a pre-existing salesperson
def add_salesperson_success_view(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST.get('fname', None)
        lname = request.POST.get('lname', None)
        address = request.POST.get('address', None)
        phoneNumber = request.POST.get('phonenumber', None)
        startdate = request.POST.get('startdate', None)
        terminationDate = request.POST.get('terminationdate')
        manager = request.POST.get('manager', None)

        try:

            temp = Salesperson.objects.get(firstName=fname, lastName=lname, startDate=startdate)

            context['error'] = 'Salesperson already exists'
            return render(request, 'directory/edit_failure.html', context)
        except:
            salesperson = Salesperson.objects.create(firstName=fname, lastName=lname, address=address,
                                                         phoneNumber=phoneNumber, startDate=startdate,
                                                         terminationDate=terminationDate, manager=manager)

    return render(request, 'directory/add_success.html', context)

