from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import flight,passengers

# Create your views here.
def home(request):
    return render(request,"airline/home.html",{
        "flights":flight.objects.all()
    })

def showcounter(request):
    return render(request,"airline/counter.html")

def flight_details(request,flight_id):
    flight_info=flight.objects.get(pk=flight_id)
    return render(request,"airline/flightdetail.html",{
        "flight":flight_info,
        "passengers":flight_info.passengers.all(),
        "non_passengers":passengers.objects.exclude(flights=flight_info).all()
    })


def book(request,flight_id):
    if request.method == 'POST':
        flight_info=flight.objects.get(pk=flight_id)
        passenger_info=passengers.objects.get(pk=request.POST["passenger"])
        passenger_info.flights.add(flight_info)
        passenger_info.save()
        return HttpResponseRedirect(reverse('flightdetails',args=(flight_id,)))
