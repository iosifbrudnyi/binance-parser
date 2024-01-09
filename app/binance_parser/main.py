import asyncio
import json
from typing import List
import uuid
from containers.base import Container
from exceptions.base import BinanceParserException
from schemas.tickers import TickerBase, TickerResponse
from services.tickers import TickerService
import websockets
from dependency_injector.wiring import Provide, inject

class BinanceParser:

    def __init__(self, url: str, timeout: int):
        self.url = url
        self.timeout = timeout

    def transform_response(self, response: TickerResponse) -> List[TickerBase]:
        return [ticker for ticker in response["result"]]

    @inject
    async def save_to_db(self, data: List[TickerBase], ticker_service: TickerService = Provide[Container.ticker_service]):
        for ticker in data:
            await ticker_service.save_db(ticker)

    async def save_to_redis(self, data: List[TickerBase], ticker_service: TickerService = Provide[Container.ticker_service]):
        await ticker_service.save_redis(data)

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

                    data = self.transform_response(response)
                    await self.save_to_db(data)
                    await self.save_to_redis(data)

                except Exception as e:
                    BinanceParserException(e)

                await asyncio.sleep(self.timeout)
