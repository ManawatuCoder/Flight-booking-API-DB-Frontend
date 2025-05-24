from django.http import HttpResponse

from .models import Airports


def populateAirports(request):
    a = Airports(
        airportCode = "NZNE",
        name = "Dairy Flats"
    )
    a.save()
    a = Airports(
        airportCode="YMML",
        name = "Melbourne"
    )
    a.save()
    a = Airports(
        airportCode="NZGB",
        name="Claris, Great Barrier Island"
    )
    a.save()
    a = Airports(
        airportCode="NZRO",
        name="Rotorua"
    )
    a.save()
    a = Airports(
        airportCode="NZCI",
        name="Tuuta, Chatham Islands"
    )
    a.save()
    a = Airports(
        airportCode="NZTL",
        name="Lake Tekapo"
    )
    a.save()

    text = '<h1>Airports Populated</h1>'
    return HttpResponse(text)