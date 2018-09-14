from django.contrib import admin

# Register your models here.
from reservation.models import Event, Reservation

admin.site.regiter(Event)
admin.site.regiter(Reservation)