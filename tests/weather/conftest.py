import json

import pytest

from weather.models import Location


@pytest.fixture
def locations_data():
    yield [
        {
            'ID': 25,
            'Name': 'Girona'
        },
        {
            'ID': 26,
            'Name': 'Salt'
        },
    ]


@pytest.fixture
def location_models(db, locations_data):
    yield [
        Location.objects.create(**{
            'code': location['ID'],
            'name': location['Name'],
        })
        for location in locations_data
    ]


@pytest.fixture
def weather_data(location_models):
    for location in location_models:
        location.weather_data = json.dumps({'data': 'weather'})
        location.weather_data_updated = '2021-02-10'
        location.save()

    yield location_models
