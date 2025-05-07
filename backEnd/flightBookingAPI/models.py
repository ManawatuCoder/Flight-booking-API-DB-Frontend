from django.db import models

def auto_increment():
    value = Flights.bookedSeats

class Flights(models.Model):
    #Arbitrary max length values, currently.
    code = models.IntegerField(primary_key=True)
    craftName = models.CharField(max_length=3, primary_key=False, default="poop")
    departTime = models.IntegerField()
    arriveTime = models.IntegerField()
    startLocation = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    # Define the t a b l e name
    class Meta:
        db_table = 'flights'

# class Planes(models.Model):
#     craftName = models.CharField(max_length=14)
#     passengers = models.IntegerField(max_length=6)
#
#     class Meta:
#         db_tables = 'Planes'
#
# class Bookings:
#     passengerID = models.IntegerField(max_length=20)
#     bookedSeats = models.IntegerField(default = 0)
#     maxBookings = models.IntegerField()
