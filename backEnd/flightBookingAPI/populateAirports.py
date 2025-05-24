from django.http import HttpResponse

from .models import Airports


def populateAirports(request):
    a = Airports(
        airportCode = "NZNE"
    )
    a.save()
    a = Airports(
        airportCode="YMML"
    )
    a.save()
    a = Airports(
        airportCode="NZGB"
    )
    a.save()
    a = Airports(
        airportCode="NZRO"
    )
    a.save()
    a = Airports(
        airportCode="NZCI"
    )
    a.save()
    a = Airports(
        airportCode="NZTL"
    )
    a.save()

    text = '<h1>Airports Populated</h1>'
    return HttpResponse(text)