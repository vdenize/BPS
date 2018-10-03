from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
