from django.db import models
from django.utils import timezone


class Location(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    weather_data = models.JSONField(null=True, blank=True)
    weather_data_updated = models.DateTimeField(null=True, blank=True)

    def set_weather_data(self, weather_data):
        self.weather_data = weather_data
        self.weather_data_updated = timezone.now()
