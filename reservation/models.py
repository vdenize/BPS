from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
