import aioredis
from databases import Database
from fastapi import Depends
from server.db.redis import get_redis
from server.services.tickers import TickerService

def ticker_service(redis: aioredis.Redis = Depends(get_redis)):
    return TickerService(redis)

