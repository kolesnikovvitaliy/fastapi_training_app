from fastapi import APIRouter
import redis

# import os
# from fastapi_cache import FastAPICache
from ....celery_worker.config import stages, STAGING_TIME
from ....celery_worker.worker import move_to_next_stage

# import redis.asyncio as redis
# from redis.asyncio.connection import ConnectionPool

redis_store = redis.Redis.from_url(url="redis://:TestTest12345678@redis_cache:6379/2")
# pool = ConnectionPool(
#         host=f"{os.environ.get("REDIS_HOST")}",
#         password=f"{os.environ.get("REDIS_PASSWORD")}",
#         port=int(f"{os.environ.get("REDIS_PORT")}"),
#         db=int(f"{os.environ.get("REDIS_STORE_DB_INDEX")}"),
#     )
# redis_store = redis.Redis(connection_pool=pool)

# redis_store = redis.Redis.from_url(REDIS_STORE_CONN_URI)
router = APIRouter(tags=["Product"])


@router.get("/buy/{name}")
async def buy(name: str):
    for i in range(0, 5):
        move_to_next_stage.apply_async((name, stages[i]), countdown=i*STAGING_TIME)
    return True


@router.get("/status/{name}")
async def status(name: str):
    return redis_store.get(name)


# @router.post("/buy/{name}")
# # async def buy(name: str):
# #     for i in range(0, 5):
# #         move_to_next_stage.apply_async((name, stages[i]), countdown=i * STAGING_TIME)
# #     return True
# async def move_to_next_stage(name="create_task_2", stage="1"):
#     redis_store.set(name, stage)
#     return stage


# @router.get("/status/{name}")
# async def status(name: str):
#     return redis_store.get(name)


# @router.get("get_add/{a}{b}")
# async def res(a: int, b: int):
#     result = add.apply(a, b)
#     return result
