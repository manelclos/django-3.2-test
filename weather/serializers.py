from rest_framework import serializers

from .models import Location


class LocationCodeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['code', 'name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['code', 'name', 'weather_data']
