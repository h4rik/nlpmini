from django.urls import path
from . import views

urlpatterns = [
       
   path('transport/',views.index,name='index'),
   path("register_driver/",views.register_driver,name="register_driver"),
   path("driver_list/",views.driver_list,name="driver_list"),
   path("hub_owner/",views.hub_owner,name="hub_owner"),
   path("hub/",views.hubs,name="hub"),
   path("trucks/",views.Trucks_view,name="trucks"),
   path("login",views.login,name="login"),
   path("log",views.log,name="log")
]
