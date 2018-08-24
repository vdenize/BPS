from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    birthday = models.DateField()
    gender = models.CharField(max_length=6)

