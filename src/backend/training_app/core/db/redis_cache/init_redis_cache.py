import os

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

import redis.asyncio as redis
from redis.asyncio.connection import ConnectionPool


pool = ConnectionPool(
        host=f"{os.environ.get("REDIS_HOST")}",
        password=f"{os.environ.get("REDIS_PASSWORD")}",
        port=int(f"{os.environ.get("REDIS_PORT")}"),
        db=int(f"{os.environ.get("REDIS_STORE_DB_INDEX")}"),
    )
redis_pool = redis.Redis(connection_pool=pool)


async def redis_cache() -> FastAPICache:
    FastAPICache.init(RedisBackend(redis_pool), prefix="fastapi-cache")
