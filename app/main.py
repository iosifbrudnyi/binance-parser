import asyncio
from contextlib import asynccontextmanager
import aioredis
from binance_parser.main import BinanceParser
from containers.base import Container
from db.db import get_db
from db.redis import get_redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import uvicorn
from fastapi import FastAPI
from config import APP_HOST, APP_PORT, BINANCE_API_URL, BINANCE_LISTEN_TIMEOUT, DATABASE_URL, REDIS_URL
from api.tickers import router as ticker_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache") 

    binance_parser = BinanceParser(url=BINANCE_API_URL, timeout=BINANCE_LISTEN_TIMEOUT)
    asyncio.create_task(binance_parser.listen())

    yield

    await redis.close()

app = FastAPI(lifespan=lifespan)
app.include_router(ticker_router, prefix="/api")

container = Container()
container.config.database_url.from_value(DATABASE_URL)
container.config.redis_url.from_value(REDIS_URL)
container.wire(modules=[__name__, "api.tickers", "binance_parser.main"])

app.container = container

def main():
    uvicorn.run(app="main:app", reload=True, host=APP_HOST, port=APP_PORT)

if __name__ == "__main__":
    main()