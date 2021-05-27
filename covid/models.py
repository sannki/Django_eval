import datetime
from django.db import models
from django.utils import timezone

class covid_db(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    aadhar = models.IntegerField(primary_key=True)
    address = models.CharField(max_length = 50)

