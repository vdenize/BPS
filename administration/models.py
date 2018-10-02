from django.db import models

# Create your models here.
from login.models import Profile


class Payments(models.Model):
    patient = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    date = models.DateField()
    amount = models.IntegerField()