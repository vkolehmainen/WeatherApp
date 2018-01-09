from django.db import models

# Create your models here.
TYPES = (
    ('SUN', 'Sunny'),
    ('RAIN', 'Rainy'),
    ('CLOUD', 'Cloudy'),
    ('SNOW', 'Snowy'),
    ('STORM', 'Stormy')
)

class City(models.Model):
    name = models.CharField(max_length=255, unique = True)
    x_coord = models.FloatField()
    y_coord = models.FloatField()

    def __str__(self):
       return self.name

class Observation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    time = models.TimeField()

    weather_type = models.CharField(
        max_length = 5,
        choices=TYPES,
        default="SUN",
    )
