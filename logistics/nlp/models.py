from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    booking_date = models.CharField(max_length=10)
    goods_type = models.CharField(max_length=20)
    weight = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
