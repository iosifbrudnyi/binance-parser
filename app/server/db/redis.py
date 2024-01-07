

import aioredis
from config import REDIS_URL


async def get_redis() -> aioredis.Redis:
    return await aioredis.Redis().from_url(REDIS_URL)