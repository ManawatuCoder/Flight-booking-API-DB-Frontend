import random

from django.db import models

def auto_increment():
    value = Flights.passengers

class Flights(models.Model):
    #Arbitrary max length values, currently.
    code = models.IntegerField(primary_key=True)
    craftName = models.CharField(max_length=3, primary_key=False, default="poop")
    departTime = models.DateTimeField()
    arriveTime = models.DateTimeField()
    startLocation = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    passengers = models.IntegerField(default = 0)

    # Define the t a b l e name
    class Meta:
        db_table = 'flights'

class Planes(models.Model):
    craftName = models.CharField(max_length=15, primary_key=True)
    maxPassengers = models.IntegerField()

    class Meta:
        db_table = 'planes'

def uniqueGenerator():
    while True:
        code = random.randint(1000000,9999999)
        if not Bookings.objects.filter(bookingRef=code).exists():
            return code

class Bookings(models.Model):
    flightCode = models.ForeignKey(Flights, to_field='code', on_delete=models.CASCADE)
    bookingRef = models.IntegerField(unique=True, default=uniqueGenerator, primary_key=True)
    passengerID = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'bookings'

class Airports(models.Model):
    airportCode = models.CharField(max_length=4)

    class Meta:
        db_table = 'airports'