from django.urls import path
from . import views

urlpatterns = [
   path("register_driver",views.register_driver,name="register_driver"),
   path("driver_list",views.driver_list,name="driver_list"),
    
]
