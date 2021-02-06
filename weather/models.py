from django.db import models


class Location(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
