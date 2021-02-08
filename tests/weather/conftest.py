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
def location_models(locations_data):
    yield [
        Location.objects.create(**{
            'code': location['ID'],
            'name': location['Name'],
        })
        for location in locations_data
    ]
