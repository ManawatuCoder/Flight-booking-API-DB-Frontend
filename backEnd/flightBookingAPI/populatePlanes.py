from django.http import HttpResponse

from .models import Planes


def populatePlanes(request):
    planes = [("SyberJet SJ30i 1", 6),
              ("Cirrus SF50 1", 4),
              ("Cirrus SF50 2", 4),
              ("HondaJet Elite 1", 5),
              ("HondaJet Elite 2", 5)]

    for name, seats in planes:
        exists = False
        if not Planes.objects.filter(craftName=name).exists:
            p = Planes(
                craftName=name,
                maxPassengers = seats
            )
            p.save()

    text = '<h1>Planes Populated</h1>'
    return HttpResponse(text)