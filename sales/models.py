from django.db import models

# Create your models here.

class SalesReport(models.Model):
    dailysales = models.IntegerField()
    dailyper = models.IntegerField()
    monthlysales = models.IntegerField()
    monthlyper = models.IntegerField()
    anualsales = models.IntegerField()
    anualper = models.IntegerField()
