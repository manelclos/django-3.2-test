import asyncio

import aiohttp
from asgiref.sync import async_to_sync

from . import api


@async_to_sync
async def update_locations_weather_data(locations):
    async with aiohttp.ClientSession() as session:
        values = await asyncio.gather(*[
            api.get_weather_data(session, location.code)
            for location in locations
        ])

        updated = 0

        for index, location in enumerate(locations):
            response = values[index]
            if response.status == 200:
                location.set_weather_data(await response.text())
                updated = updated + 1

    # avoid Resource Warning: https://github.com/aio-libs/aiohttp/issues/1115
    await asyncio.sleep(0.1)

    return updated
