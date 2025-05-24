"""
URL configuration for flightBookingAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views, API, populatePlanes, populateFlights, populateAirports

urlpatterns = [
    path('flightslist/', API.flightslist, name='flightslist'),
    path('form/', views.form, name='form'),
    path('flights/', API.flightslist, name='flights'),
    path('flightBookingAPI', views.hello, name='hello'),
    path('admin/', admin.site.urls),
    path("bookings/", views.bookings, name='bookings'),
    path("bookflight/", API.book),
    path("unbookflight/", API.unbook),
    path('populateplanes/', populatePlanes.populatePlanes),
    path('populateflights/', populateFlights.populateFlights),
    path('withinperiod/', API.withinPeriod),
    path('populateairports/', populateAirports.populateAirports),
    path('airportlist/', API.airportlist, name='airportlist'),
]
