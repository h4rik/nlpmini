from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect
# Create your views here.
def register_driver(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        address = request.POST['address']
        aadhar = request.POST['aadhar']
        license = request.POST['license']
        phone = request.POST['phone']
        
        driver = Driver(name=name, dob=dob, address=address, aadhar=aadhar, license=license, phone=phone)
        driver.save()

        return redirect('driver_list')
    
    return render(request, 'driver_register.html')

def driver_list(request):
    drivers=Driver.objects.all()
    return render(request,"driver_list.html",{"drivers":drivers})


