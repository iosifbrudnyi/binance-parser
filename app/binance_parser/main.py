import asyncio
import json
import logging
import pickle
from typing import List
import uuid
import aioredis
from databases import Database
from exceptions.base import BinanceParserException
from schemas.tickers import TickerBase, TickerResponse
from services.tickers import TickerService
import websockets

class BinanceParser:
    def __init__(self, url: str, timeout: int, db: Database, redis_db: aioredis.Redis):
        self.url = url
        self.timeout = timeout
        self.ticker_service: TickerService = TickerService(db=db, redis_db=redis_db)

    def transform_response(self, response: TickerResponse) -> List[TickerBase]:
        return [ticker for ticker in response["result"]]

    async def save_to_db(self, data: List[TickerBase]):
        for ticker in data:
            await self.ticker_service.save_db(ticker)

    async def save_to_redis(self, data: List[TickerBase]):
        await self.ticker_service.save_redis(data)

    async def listen(self):
        async with websockets.connect(self.url) as websocket:
            while True:
                sub_request = {
                    "method": "ticker.price",
                    "id": str(uuid.uuid4())
                }

                try:
                    await websocket.send(json.dumps(sub_request))                
                    response: TickerResponse = json.loads(await websocket.recv())
                except Exception as e:
                    BinanceParserException(e)

                data = self.transform_response(response)
                await self.save_to_db(data)
                await self.save_to_redis(data)

                await asyncio.sleep(self.timeout)
