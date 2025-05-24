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
    try:
        flight = Flights.objects.get(code=code)
        craft = flight.craftName
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
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def flightslist(request):
    flightsList = []

    for entry in Flights.objects.all():
        flightsList.append({
            "code": entry.code,
            "craftName": entry.craftName,
            "departTime": entry.departTime,
            "arriveTime": entry.arriveTime,
            "startLocation": entry.startLocation,
            "destination": entry.destination,
            "passengers": entry.passengers,
        })
    return JsonResponse(flightsList, safe=False)


def withinPeriod(request):
    try:
        start = timezone.make_aware(parse_datetime(request.GET.get("start")))
        end = timezone.make_aware(parse_datetime(request.GET.get("end")))
        depart = request.GET.get("departure")
        arrive = request.GET.get("arrival")

        flights = Flights.objects.filter(departTime__range=(start, end), destination = depart, startLocation = arrive)
        text = '<h1>This is a response</h1>'

        response = []
        for flight in flights:
            response.append({
                'code': flight.code,
                'craftName': flight.craftName,
                'departTime': flight.departTime,
                'arriveTime': flight.arriveTime,
                'startLocation': flight.startLocation,
                'destination': flight.destination,
                'passengers': flight.passengers,
                'duration': str(flight.arriveTime - flight.departTime)
            })

        if not response:
            return JsonResponse({'status': 'no results', 'message': 'No flights found matching the specified request'}, status=404)
    except:
        return JsonResponse({'status': 'no results', 'message': 'No flights found matching the specified request'},
                            status=404)
    return JsonResponse(response, safe=False)

def airportlist(request):
    pdata = {}

    for entry in Airports.objects.all():
        pdata[entry.airportCode] = entry.name
    return JsonResponse(pdata)