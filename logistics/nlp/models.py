from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    aadhar = models.CharField(max_length=12)
    license = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class hubowner(models.Model):   #i have changed this and below class names form warehouseOwner and warehouse to hubowner and hub
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    aadhar = models.CharField(max_length=12)
    def __str__(self):
        return self.name
    
class hub(models.Model):  #hub or warehouse both are same  
    owner=models.ForeignKey(hubowner,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    pincode=models.CharField(max_length=6)
    hub_storage_capacity=models.FloatField()
    def __str__(self):
        return self.name
    
    
class trucks(models.Model):
    driver=models.ForeignKey(Driver,on_delete=models.CASCADE)
    number=models.CharField(max_length=10)
    truck_storage_capacity=models.FloatField()
    def __str__(self):
        return self.number