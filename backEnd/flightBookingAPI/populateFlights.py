import datetime
import random

from django.http import HttpResponse
from django.utils import timezone

from .models import Flights, Planes


def populateFlights(request):
#Melb
    SyberDepart1 = timezone.make_aware(datetime.datetime(2025, 5, 23, 10, 0, 0))
    SyberArrive1 = timezone.make_aware(datetime.datetime(2025, 5, 23, 14, 0, 0))

    SyberDepart2 = timezone.make_aware(datetime.datetime(2025,5,25,16,0,0))
    SyberArrive2 = timezone.make_aware(datetime.datetime(2025,5,25,20,0,0))

#Roto
    Cirrus1Depart1 = timezone.make_aware(datetime.datetime(2025, 5, 19, 6,0,0))
    Cirrus1Arrive1 = timezone.make_aware(datetime.datetime(2025, 5, 19, 7, 0, 0))

    Cirrus1Depart2 = timezone.make_aware(datetime.datetime(2025, 5, 19, 7, 30, 0))
    Cirrus1Arrive2 = timezone.make_aware(datetime.datetime(2025, 5, 19, 8, 30, 0))

#Great Barrier
    Cirrus2Depart1 = timezone.make_aware(datetime.datetime(2025, 5, 19, 8, 0, 0))
    Cirrus2Arrive1 = timezone.make_aware(datetime.datetime(2025, 5, 19, 8, 30, 0))

    Cirrus2Depart2 = timezone.make_aware(datetime.datetime(2025, 5, 20, 8, 0, 0))
    Cirrus2Arrive2 = timezone.make_aware(datetime.datetime(2025, 5, 20, 8, 30, 0))

#Chatham
    HondaJet1Depart1 = timezone.make_aware(datetime.datetime(2025, 5, 20, 12, 0, 0))
    HondaJet1Arrive1 = timezone.make_aware(datetime.datetime(2025, 5, 20, 13, 45, 0))

    HondaJet1Depart2 = timezone.make_aware(datetime.datetime(2025, 5, 21, 12, 0, 0))
    HondaJet1Arrive2 = timezone.make_aware(datetime.datetime(2025, 5, 21, 13, 45, 0))

#tekapo
    HondaJet2Depart1 = timezone.make_aware(datetime.datetime(2025, 5, 19, 12, 0, 0))
    HondaJet2Arrive1 = timezone.make_aware(datetime.datetime(2025, 5, 19, 13, 20, 0))

    HondaJet2Depart2 = timezone.make_aware(datetime.datetime(2025, 5, 20, 12, 0, 0))
    HondaJet2Arrive2 = timezone.make_aware(datetime.datetime(2025, 5, 20, 13, 20, 0))



        #******************************
        #SyberJet DF to Melb
        #******************************
    for i in range(12):
        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)
        f = Flights(
            craftName="SyberJet SJ30i 1",
            code=randCode,
            departTime = SyberDepart1,
            arriveTime = SyberArrive1,
            startLocation = "NZNE",
            destination = "YMML",
            passengers = 0,
            price = 500
        )
        f.save()
        SyberDepart1 = SyberDepart1 + datetime.timedelta(days = 7)
        SyberArrive1 = SyberArrive1 +  + datetime.timedelta(days = 7)



        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)
        f = Flights(
            craftName="SyberJet SJ30i 1",
            code=randCode,
            departTime = SyberDepart2,
            arriveTime = SyberArrive2,
            startLocation = "YMML",
            destination = "NZNE",
            passengers = 0,
            price=500
        )
        f.save()
        SyberDepart2 += datetime.timedelta(days = 7)
        SyberArrive2 += datetime.timedelta(days = 7)

    # ******************************
    # Cirrus1 DF to Roto
    # ******************************

    for i in range(60):
        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="Cirrus SF50 1",
            code=randCode,
            departTime=Cirrus1Depart1,
            arriveTime=Cirrus1Arrive1,
            startLocation="NZNE",
            destination="NZRO",
            passengers=0,
            price=300
        )
        f.save()


        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="Cirrus SF50 1",
            code=randCode,
            departTime=Cirrus1Depart2,
            arriveTime=Cirrus1Arrive2,
            startLocation="NZRO",
            destination="NZNE",
            passengers=0,
            price=300
        )
        f.save()

    #Later the same day
        Cirrus1Depart1 += datetime.timedelta(hours=11)
        Cirrus1Arrive1 += datetime.timedelta(hours=11)

        Cirrus1Depart2 += datetime.timedelta(hours=11)
        Cirrus1Arrive2 += datetime.timedelta(hours=11)

        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="Cirrus SF50 1",
            code=randCode,
            departTime=Cirrus1Depart1,
            arriveTime=Cirrus1Arrive1,
            startLocation="NZNE",
            destination="NZRO",
            passengers=0,
            price=300
        )
        f.save()


        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="Cirrus SF50 1",
            code=randCode,
            departTime=Cirrus1Depart2,
            arriveTime=Cirrus1Arrive2,
            startLocation="NZRO",
            destination="NZNE",
            passengers=0,
            price=300
        )
        f.save()


        Cirrus1Depart1 += datetime.timedelta(hours=13)
        Cirrus1Arrive1 += datetime.timedelta(hours=13)

        Cirrus1Depart2 += datetime.timedelta(hours=13)
        Cirrus1Arrive2 += datetime.timedelta(hours=13)



    # ******************************
    # Cirrus2 DF to Great Barrier
    # ******************************

    for i in range(36):
        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="Cirrus SF50 2",
            code=randCode,
            departTime=Cirrus2Depart1,
            arriveTime=Cirrus2Arrive1,
            startLocation="NZNE",
            destination="NZGB",
            passengers=0,
            price=400
        )
        f.save()

        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="Cirrus SF50 2",
            code=randCode,
            departTime=Cirrus2Depart2,
            arriveTime=Cirrus2Arrive2,
            startLocation="NZGB",
            destination="NZNE",
            passengers=0,
            price=400
        )
        f.save()

        if i%3 == 0:
            Cirrus2Depart1 += datetime.timedelta(days=2)
            Cirrus2Arrive1 += datetime.timedelta(days=2)

            Cirrus2Depart2 += datetime.timedelta(days=2)
            Cirrus2Arrive2 += datetime.timedelta(days=2)
        else:
            Cirrus2Depart1 += datetime.timedelta(days=3)
            Cirrus2Arrive1 += datetime.timedelta(days=3)

            Cirrus2Depart2 += datetime.timedelta(days=3)
            Cirrus2Arrive2 += datetime.timedelta(days=3)

    # ******************************
    # HondaJet1 DF to Tuuta
    # ******************************

    for i in range(24):
        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="HondaJet Elite 1",
            code=randCode,
            departTime=HondaJet1Depart1,
            arriveTime=HondaJet1Arrive1,
            startLocation="NZNE",
            destination="NZCI",
            passengers=0,
            price=400
        )
        f.save()

        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="HondaJet Elite 1",
            code=randCode,
            departTime=HondaJet1Depart2,
            arriveTime=HondaJet1Arrive2,
            startLocation="NZCI",
            destination="NZNE",
            passengers=0,
            price=400
        )
        f.save()

        # print(HondaJet1Depart1.strftime('%A'))
        # print(HondaJet1Depart2.strftime('%A'))

        if i%2 != 0:
            HondaJet1Depart1 += datetime.timedelta(days=4)
            HondaJet1Arrive1 += datetime.timedelta(days=4)

            HondaJet1Depart2 += datetime.timedelta(days=4)
            HondaJet1Arrive2 += datetime.timedelta(days=4)
        else:
            HondaJet1Depart1 += datetime.timedelta(days=3)
            HondaJet1Arrive1 += datetime.timedelta(days=3)

            HondaJet1Depart2 += datetime.timedelta(days=3)
            HondaJet1Arrive2 += datetime.timedelta(days=3)


    # ******************************
    # HondaJet2 DF to Tekapo
    # ******************************

    for i in range(12):
        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="HondaJet Elite 2",
            code=randCode,
            departTime=HondaJet2Depart1,
            arriveTime=HondaJet2Arrive1,
            startLocation="NZNE",
            destination="NZCI",
            passengers=0,
            price=200
        )
        f.save()

        randCode = random.randint(1000000, 9999999)
        while Flights.objects.filter(code=randCode).exists():
            randCode = random.randint(1000000, 9999999)

        f = Flights(
            craftName="HondaJet Elite 2",
            code=randCode,
            departTime=HondaJet2Depart2,
            arriveTime=HondaJet2Arrive2,
            startLocation="NZCI",
            destination="NZNE",
            passengers=0,
            price=200
        )
        f.save()

        HondaJet2Depart1 += datetime.timedelta(days=7)
        HondaJet2Arrive1 += datetime.timedelta(days=7)

        HondaJet2Depart2 += datetime.timedelta(days=7)
        HondaJet2Arrive2 += datetime.timedelta(days=7)


    text = '<h1>Flights Populated</h1>'
    return HttpResponse(text)