import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Location
from .serializers import LocationCodeNameSerializer, LocationSerializer


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()

    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationCodeNameSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Location.objects.all()
        user = get_object_or_404(queryset, code=pk)
        serializer = LocationSerializer(user)
        return Response(serializer.data)


@api_view()
def get_location_weather_data(request, code):
    obj = get_object_or_404(Location, code=code)
    if obj.weather_data is None:
        return Response({'error': 'data not yet available'})

    return Response(json.loads(obj.weather_data))


@api_view()
async def get_location_weather_data_raw(request, code):
    # print('*** ASYNC ***')
    obj = get_object_or_404(Location, code=code)
    if obj.weather_data is None:
        return Response({'error': 'data not yet available'})

    # Skip json loads / dumps
    return HttpResponse(obj.weather_data, content_type='application/json')
