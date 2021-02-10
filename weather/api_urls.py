from django.urls import path

from rest_framework.routers import DefaultRouter

from . import api

router = DefaultRouter()
router.register(r'location', api.LocationViewSet, basename='location')
urlpatterns = router.urls

urlpatterns.extend([
    path('location_data/<int:code>/', api.get_location_weather_data, name='api_get_location_weather_data'),
    path('location_data/<int:code>/raw/', api.get_location_weather_data_raw, name='api_get_location_weather_data_raw'),
])
