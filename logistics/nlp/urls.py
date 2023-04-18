from django.urls import path
from . import views

urlpatterns = [
    path('transport/',views.index,name='index'),
    path('book_shipment/', views.book_shipment, name='book_shipment'),
    
]
