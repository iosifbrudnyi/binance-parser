from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import uvicorn
from fastapi import FastAPI
from config import REDIS_URL
from server.api.tickers import router as ticker_router
import aioredis

app = FastAPI()
app.include_router(ticker_router, prefix="/api")

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

@app.get("/")
def root():
    return {"success": "true"}

if __name__ == "__main__":
    uvicorn.run(app="server.main:app", reload=True, host="0.0.0.0", port=8000)