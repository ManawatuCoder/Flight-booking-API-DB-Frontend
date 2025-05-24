import random

from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from .models import Flights, Airports, Planes, Bookings


def unbook(request):
    code = request.GET.get('code')

    try:
        booking = Bookings.objects.get(bookingRef=code)
        flight = Flights.objects.get(code=booking.flightCode.code)
        flight.passengers -= 1
        booking.delete()
        flight.save()
        return JsonResponse({'status': 'success', 'message': f'Booking {code} deleted.'})
    except Bookings.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': f'Booking {code} not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)



def book(request):
    code = (request.GET.get('code'))
    customerName = request.GET.get('name')
    flight = Flights.objects.get(code=code)
    craft = flight.craftName
    print(code)
    passengerCount = Planes.objects.get(craftName=craft).maxPassengers

    randCode = random.randint(1000000, 9999999)
    while Bookings.objects.filter(bookingRef=randCode).exists():
        randCode = random.randint(1000000, 9999999)


    if flight.passengers < passengerCount:
        b = Bookings(
            bookingRef=randCode,
            passengerID=customerName,
            flightCode=flight
        )
        b.save()
        flight.passengers += 1
        flight.save()
        text = '<h1>Booking Made</h1>'
    else:
        text = '<h1>Flight Full: No Booking Made</h1>'
    return HttpResponse(text)

def flightslist(request):
    pdata = {}

    for entry in Flights.objects.all():
        pdata[entry.code] = entry.code
        pdata[entry.craftName] = entry.craftName
    return JsonResponse(pdata)

def withinPeriod(request):
    start = timezone.make_aware(parse_datetime(request.GET.get("start")))
    end = timezone.make_aware(parse_datetime(request.GET.get("end")))
    depart = request.GET.get("departure")
    arrive = request.GET.get("arrival")

    flights = Flights.objects.filter(departTime__range=(start, end), destination = depart, startLocation = arrive)
    # for item in flights:
    #     print(item)
    text = '<h1>This is a response</h1>'
    response = list(flights.values())
    return JsonResponse(response, safe=False)

def airportlist(request):
    pdata = {}

    for entry in Airports.objects.all():
        pdata[entry.airportCode] = entry.name
    return JsonResponse(pdata)