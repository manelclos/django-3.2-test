import json

import pytest

from django.urls import reverse


def test_location_rest_api_list(app, weather_data):
    url = reverse('location-list')
    response = app.get(url)
    data = response.json

    assert len(data) == 2
    assert data == [{'code': 25, 'name': 'Girona'}, {'code': 26, 'name': 'Salt'}]


def test_location_rest_api_detail(app, weather_data):
    url = reverse('location-detail', args=[weather_data[0].code])
    response = app.get(url)

    assert json.loads(response.content) == {'code': 25, 'name': 'Girona', 'weather_data': '{"data": "weather"}'}


@pytest.mark.parametrize("url_name", ['api_get_location_weather_data', 'api_get_location_weather_data_raw'])
def test_get_location_weather_data_not_available(app, location_models, url_name):
    url = reverse(url_name, args=[location_models[0].code])

    response = app.get(url)

    assert json.loads(response.content) == {'error': 'data not yet available'}


@pytest.mark.parametrize("url_name", ['api_get_location_weather_data', 'api_get_location_weather_data_raw'])
def test_get_location_weather_data(app, weather_data, url_name):
    url = reverse(url_name, args=[weather_data[0].code])

    response = app.get(url)

    assert json.loads(response.content) == {'data': 'weather'}
