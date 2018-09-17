from django.contrib import admin

# Register your models here.
from reservation.models import Event, Reservation

admin.site.register(Event)
admin.site.register(Reservation)