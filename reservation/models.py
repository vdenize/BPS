from django.db import models

from login.models import Profile


class Event(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Reservation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
