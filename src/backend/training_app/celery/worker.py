import os
import time
import redis

redis_store = redis.Redis.from_url("redis://redis:TestTest12345678@redis_cache:6379/0")

# from celery import Celery
from .app import celery_app


@celery_app.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@celery_app.task
def move_to_next_stage(name="create_task_2", stage="1"):
    redis_store.set(name, stage)
    return stage
