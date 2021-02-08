from django.conf import settings


async def get_weather_data(session, id):
    lan = 'es'
    url = f'https://api.tutiempo.net/json/?lan={lan}&apid={settings.API_KEY}&lid={id}'

    async with session.get(url) as response:
        await response.text()
        return response
