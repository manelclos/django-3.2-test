import asyncio

import aiohttp
from asgiref.sync import async_to_sync

from . import weather_api


@async_to_sync
async def update_locations_weather_data(locations):
    async with aiohttp.ClientSession() as session:
        values = await asyncio.gather(*[
            weather_api.get_weather_data(session, location.code)
            for location in locations
        ])

        updated = 0

        for index, location in enumerate(locations):
            response = values[index]
            if response.status == 200:
                data = await response.text()
                if 'error' in data:
                    location.error = data
                    continue
                location.set_weather_data(data)
                location.error = None
                updated = updated + 1
            else:
                location.error = f'Status {response.status}: {data})'

    # avoid Resource Warning: https://github.com/aio-libs/aiohttp/issues/1115
    await asyncio.sleep(0.1)

    return updated
