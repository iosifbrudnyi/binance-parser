import asyncio
from contextlib import asynccontextmanager
from binance_parser.main import BinanceParser
from db.db import get_db
from db.redis import get_redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import uvicorn
from fastapi import FastAPI
from config import APP_HOST, APP_PORT, BINANCE_API_URL, BINANCE_LISTEN_TIMEOUT
from api.tickers import router as ticker_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = await get_redis()
    db = await get_db()

    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache") 
    binance_parser = BinanceParser(BINANCE_API_URL, BINANCE_LISTEN_TIMEOUT, db, redis)
    asyncio.create_task(binance_parser.listen())

    yield

    await redis.close()




app = FastAPI(lifespan=lifespan)
app.include_router(ticker_router, prefix="/api")

def main():
    uvicorn.run(app="main:app", reload=True, host=APP_HOST, port=APP_PORT)

if __name__ == "__main__":
    main()