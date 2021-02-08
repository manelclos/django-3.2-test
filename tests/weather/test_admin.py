import json

import mock

from django.urls import reverse


class MockSession:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass


class MockResponse:
    def __init__(self, text, status):
        self._text = text
        self.status = status

    async def text(self):
        return self._text

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self


def test_staff_user(app, staff_user):
    url = reverse('admin:weather_location_changelist')
    app.get(url, user=staff_user, status=403)


def test_location_user(app, location_user):
    url = reverse('admin:weather_location_changelist')
    app.get(url, user=location_user, status=200)


@mock.patch('weather.utils.aiohttp.ClientSession')
def test_action_update_weather_data(session_mock, app, location_user, location_models):
    data = {'data': 'example_data'}
    resp = MockResponse(json.dumps(data), 200)

    session_mock.return_value = MockSession()
    session_mock.return_value.get = mock.MagicMock(return_value=resp)

    for location in location_models:
        assert location.weather_data is None

    url = reverse('admin:weather_location_changelist')
    response = app.get(url, user=location_user, status=200)
    form = response.forms['changelist-form']

    for checkbox in form.fields['_selected_action']:
        checkbox.checked = True

    form['action'] = 'update_weather_data'
    response = form.submit().follow()

    for location in location_models:
        location.refresh_from_db()
        assert location.weather_data == json.dumps({'data': 'example_data'})

    assert f'Weather data updated for {len(location_models)} locations' in str(response.content)
