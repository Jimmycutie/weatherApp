from django.db import models

class WeatherData(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    conditions = models.CharField(max_length=200)

    def __str__(self):
        return self.location
