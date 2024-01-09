

from typing import AsyncIterator
import aioredis

async def get_redis(redis_url: str) -> AsyncIterator[aioredis.Redis]:
    r = await aioredis.Redis().from_url(redis_url)
    try: 
        yield r
    finally:
        await r.close()