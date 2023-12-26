import redis

# import redis.asyncio as redis
# from redis.asyncio.connection import ConnectionPool

# import time
from .config import REDIS_STORE_CONN_URI

# from .config import (
#     REDIS_HOST,
#     REDIS_PASSWORD,
#     REDIS_PORT,
#     REDIS_STORE_DB_INDEX,
# )
from .app import celery_app


# pool = ConnectionPool(
#     host=REDIS_HOST,
#     password=REDIS_PASSWORD,
#     port=int(REDIS_PORT),
#     db=int(REDIS_STORE_DB_INDEX),
# )
# redis_store = redis.Redis(connection_pool=pool)

# redis_store = redis.Redis.from_url(url="redis://:TestTest12345678@redis_cache:6379/2")
redis_store = redis.Redis.from_url(url=REDIS_STORE_CONN_URI)


@celery_app.task
def move_to_next_stage(name, stage):
    redis_store.set(name, stage)
    return stage

