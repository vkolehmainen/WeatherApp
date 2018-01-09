from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=255, unique = True)
    x_coord = models.FloatField()
    y_coord = models.FloatField()

class Observation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    time = models.TimeField()
