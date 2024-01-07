import asyncio
from contextlib import asynccontextmanager
from binance_parser.main import BinanceParser
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from server.db.redis import get_redis
import uvicorn
from fastapi import Depends, FastAPI
from config import BINANCE_API_URL, BINANCE_LISTEN_TIMEOUT
from server.api.tickers import router as ticker_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = await get_redis()

    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache") 

    binance_parser = BinanceParser(BINANCE_API_URL, BINANCE_LISTEN_TIMEOUT, redis)
    asyncio.create_task(binance_parser.listen())

    yield

    redis.close()


app = FastAPI(lifespan=lifespan)
app.include_router(ticker_router, prefix="/api")

@app.get("/")
async def root():
    return {"success": "true"}


def main():
    uvicorn.run(app="server.main:app", reload=True, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()