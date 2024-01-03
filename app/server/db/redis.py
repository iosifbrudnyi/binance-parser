

import aioredis
from config import REDIS_URL
import redis


async def get_redis() -> redis.Redis:
    return redis.Redis().from_url(REDIS_URL)