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


import heapq

def find_shortest_path(from_city, to_city):
    cities = ['Pune', 'Bangalore', 'Chennai', 'Ahmedabad', 'Delhi', 'Surat', 'Hyderabad', 'Kolkata', 'Mumbai']
    adjacency_matrix = [        
        [0, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0]
    ]
    
    from_city_index = cities.index(from_city)
    to_city_index = cities.index(to_city)
    
    distances = [float('inf')] * len(cities)
    distances[from_city_index] = 0
    
    pq = [(0, from_city_index)]
    
    while pq:
        distance, city_index = heapq.heappop(pq)
        
        if city_index == to_city_index:
            break
        
        for i in range(len(cities)):
            if adjacency_matrix[city_index][i] == 1:
                new_distance = distance + 1
                if new_distance < distances[i]:
                    distances[i] = new_distance
                    heapq.heappush(pq, (new_distance, i))
    
    if distances[to_city_index] == float('inf'):
        return f"No path found between {from_city} and {to_city}"
    
    path = [to_city_index]
    current = to_city_index
    
    while current != from_city_index:
        for i in range(len(cities)):
            if adjacency_matrix[i][current] == 1 and distances[i] == distances[current] - 1:
                path.append(i)
                current = i
                break
    
    path.reverse()
    
    return " -> ".join(cities[i] for i in path)


def log(request):
    if request.method=="POST":
        from_city=request.POST["from_city"]
        to_city=request.POST["to_city"]
        driver_list=trucks.objects.filter(location=from_city)
        return render(request,"log.html",{"path":find_shortest_path(from_city,to_city),"location":from_city,"drivers":driver_list})
    return render(request,"log.html")




