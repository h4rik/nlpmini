from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking

# Create your views here.
@login_required
def book_shipment(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        booking_date = request.POST.get('booking_date')
        goods_type = request.POST.get('goods_type')
        weight = request.POST.get('weight')
        user = request.user

        booking = Booking.objects.create(
            source=source,
            destination=destination,
            booking_date=booking_date,
            goods_type=goods_type,
            weight=weight,
            user=user
        )

        messages.success(request, 'Your booking has been confirmed!')

    return render(request, 'book_shipment.html')

def index(request):
    return render(request, 'index.html')