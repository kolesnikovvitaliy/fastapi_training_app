import redis

# import redis.asyncio as redis
# import time
# from .config import REDIS_STORE_CONN_URI
from .app import celery_app

# import redis.asyncio as redis
# from redis.asyncio.connection import ConnectionPool

redis_store = redis.Redis.from_url(url="redis://:TestTest12345678@redis_cache:6379/2")


@celery_app.task
def move_to_next_stage(name, stage):
    redis_store.set(name, stage)
    return stage


# pool = ConnectionPool(
#         host=f"{os.environ.get("REDIS_HOST")}",
#         password=f"{os.environ.get("REDIS_PASSWORD")}",
#         port=int(f"{os.environ.get("REDIS_PORT")}"),
#         db=int(f"{os.environ.get("REDIS_STORE_DB_INDEX")}"),
#     )
# redis_store = redis.Redis(connection_pool=pool)
# from celery import Celery
# from .app import celery_app


# @celery_app.task
# def move_to_next_stage(name, stage):
#     redis_store.set(name, stage)
#     return stage


# @celery_app.task(name="create_task")
# def create_task(task_type):
#     time.sleep(int(task_type) * 10)
#     return True


# @celery_app.task
# async def move_to_next_stage(name="create_task_2", stage="1"):
#     redis_store.set(name, stage)
#     return stage


# @celery_app.task
# def add(x: int, y: int):
#     return x + y
