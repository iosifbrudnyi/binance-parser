import asyncio
import json
import pickle
import uuid
from server.schemas.tikcers import TickerResponse
import websockets
import redis

class BinanceParser:
    def __init__(self, url: str, timeout: int, redis_db: redis.Redis):
        self.url: str = url
        self.timeout: int = timeout
        self.redis_db: redis.Redis = redis_db

    def save_to_redis(self, response: TickerResponse):
        d = {}
        for r in response["result"]:
            d[r["symbol"]] = r["price"]
        
        d = pickle.dumps(d)

        self.redis_db.set("tickers", d)

    async def listen(self):
        async with websockets.connect(self.url) as websocket:
            while True:
                sub_request = {
                    "method": "ticker.price",
                    "id": str(uuid.uuid4())
                }
                await websocket.send(json.dumps(sub_request))
                resposne = json.loads(await websocket.recv())

                self.save_to_redis(resposne)

                await asyncio.sleep(self.timeout)
