import asyncio
import logging
from aiohttp import ClientSession
from binance_parser.db import insert_or_update_data
from server.db.db import database
from config import BINANCE_API_URL, BINANCE_LISTEN_TIMEOUT

TICKER_URL = "ticker/price"


async def fetch_ticker(session):
    async with session.get(BINANCE_API_URL + TICKER_URL) as response:
        return await response.json()


async def listen():
    await database.connect()
    session = ClientSession()

    try:
        while True:
            try:
                data = await fetch_ticker(session)
                logging.info(data)

                for ticker in data:
                    await insert_or_update_data(database, {"symbol": ticker["symbol"], "price": ticker["price"]})

                await asyncio.sleep(BINANCE_LISTEN_TIMEOUT)
            except Exception as e:
                logging.exception(e)
    finally:
        await session.close()
        await database.disconnect()


if __name__ == "__main__":
    asyncio.run(listen())
