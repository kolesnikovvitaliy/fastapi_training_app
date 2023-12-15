import os

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

import redis.asyncio as redis
from redis.asyncio.connection import ConnectionPool


async def redis_cache() -> FastAPICache:
    pool = ConnectionPool(
        host=f"{os.environ.get("REDIS_HOST")}",
        password=f"{os.environ.get("REDIS_PASSWORD")}",
        port=int(f"{os.environ.get("REDIS_PORT")}"),
        db=0,
    )
    redis_cache = redis.Redis(connection_pool=pool)
    FastAPICache.init(RedisBackend(redis_cache), prefix="fastapi-cache")
