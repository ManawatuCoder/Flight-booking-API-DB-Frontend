from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Flights, Bookings


def hello(request):
    text = '<h1>Welcome to my app!</h1>Nice to see you here!!'
    return HttpResponse(text)

def form(request):
    return render(request, 'form.html', {})

def flights(request):
    f = Flights(
        code = request.POST['code'],
        craftName = request.POST['craftName'],
        departTime = request.POST['departTime'],
        arriveTime = request.POST['arriveTime'],
        startLocation = request.POST['startLocation'],
        destination = request.POST['destination']
    )
    f.save()
    text = '<h1>Done</h1>'
    return HttpResponse(text)

def bookings(request):
    code = 1
    for entry in Flights.objects.all():
        code = entry.code
        break

    b = Bookings(
        passengerID=request.POST['passengerID'],
        flightCode_id = code
    )
    b.save()
    text = '<h1>Done</h1>'
    return HttpResponse(text)
