from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Flights


def hello(request):
    text = '<h1>Welcome to my app!</h1>Nice to see you here!!'
    return HttpResponse(text)

def form(request):
    return render(request, 'form.html', {})

def flights(request):
    f = Flights(
    code = request.POST['code'],
    ucode = int(request.POST['ucode']),
    hcode = request.POST['hcode'],
    description = request.POST['descr'])
    f.save()
    text = '<h1>Done</h1>'
    return HttpResponse(text)

def flightslist(request):
    pdata = {}

    for entry in Flights.objects.all():
        pdata[entry.code] = entry.description
        pdata[entry.ucode] = entry.hcode
    return JsonResponse(pdata)