from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from .models import Flights, Airports


def book(request):
    b = (request.POST['code'])
    b = request.readline
    print(b)
    text = '<h1>Done</h1>'
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