from django.contrib import admin, messages

from .models import Location
from .utils import update_locations_weather_data


@admin.action(description='Update weather data for selected locations')
def update_weather_data(modeladmin, request, queryset):
    locations = list(queryset)

    updated = update_locations_weather_data(locations)
    Location.objects.bulk_update(locations, ['weather_data', 'weather_data_updated', 'error'])
    messages.info(request, f'Weather data updated for {updated} locations')

    total = len(locations)
    if updated < total:
        messages.error(request, f'Weather data update failed for {total - updated} locations')


@admin.action(description='Clear weather data for selected locations')
def clear_weather_data(modeladmin, request, queryset):
    queryset.update(weather_data=None, weather_data_updated=None)
    messages.info(request, f'Weather data cleared for {queryset.count()} locations')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'weather_data_updated')
    search_fields = ('code', 'name')
    list_filter = ('weather_data_updated', ('error', admin.EmptyFieldListFilter))
    actions = [clear_weather_data, update_weather_data]
