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

def index(request):
    return render(request, 'index.html')

def hub_owner(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        aadhar = request.POST['aadhar']
        
        
        hub_owner = hubowner(name=name, address=address, phone=phone, email=email, aadhar=aadhar)
        hub_owner.save()

        return redirect('driver_list')
    
    return render(request,'hub_owner_signup.html')

def hubs(request):
    if request.method == 'POST':
        owner=request.POST["owner_name"]
        name = request.POST['name']
        city=request.POST["hub_city"]
        address = request.POST['address']
        pincode = request.POST['pincode']
        storage_capacity = request.POST['storage_capacity']
        
        
        Hub = hub(owner=owner,name=name,city=city, address=address, pincode=pincode, hub_storage_capacity=storage_capacity)
        Hub.save()
    return render(request,'hubs_register.html')

def Trucks_view(request):
    if request.method == 'POST':
        name = request.POST['driver_name']
        vehicle_number = request.POST['vehicle_number']
        truck_capacity = request.POST['truck_capacity']

        
        Trucks = trucks(driver=name , number=vehicle_number, truck_storage_capacity=truck_capacity)
        Trucks.save()
    return render(request,'truck_register.html')


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if hubowner.objects.filter(name=username).exists():
            owner=hubowner.objects.get(name=username)
            if password==owner.password:
                return redirect("log")
            else:
                message="Invalid credentials!"
                return render(request,"login.html",{"message":message})
        else:
            message="User does not exist!"
            return render(request,"login.html",{"message":message})
    else:
        return render(request,"login.html")
    
def log(request):
    if request.method=="POST":
        location=request.POST["location"]
        return render(request,"log.html",{"location":location})
    return render(request,"log.html")