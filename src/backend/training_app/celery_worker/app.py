from celery import Celery


class MyCelery(Celery):
    def gen_task_name(self, name, module):
        if module.endswith(".worker") and module.startswith("training_app"):
            module = module[13:]
        return super().gen_task_name(name, module)


# app = MyCelery('main')
# import os
# from .config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

# import redis.asyncio as redis
# from redis.asyncio.connection import ConnectionPool
# celery_app = Celery(
#     "celery_worker",
#     broker=CELERY_BROKER_URL,
#     backend="redis://redis:TestTest12345678@redis_cache:6379/0",
# )
# redis_store = redis.Redis.from_url("redis://redis:TestTest12345678@redis_cache:6379/1")
# pool = ConnectionPool(
#         host=f"{os.environ.get("REDIS_HOST")}",
#         password=f"{os.environ.get("REDIS_PASSWORD")}",
#         port=int(f"{os.environ.get("REDIS_PORT")}"),
#         db=int(f"{os.environ.get("REDIS_STORE_DB_INDEX")}"),
#     )
# redis_store = redis.Redis(connection_pool=pool)

celery_app = MyCelery(
    "app",
    broker="amqp://guest:guest@rabbitmq_broker:5672",
    backend="redis://:TestTest12345678@redis_cache:6379/1",
    broker_api="http://guest:guest@rabbitmq_broker:15672/api/vhost",
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    include=["celery_worker.worker"],
    broker_transport_options={
        "max_retries": 1,
        "visibility_timeout": 365 * 24 * 60 * 60,
    },
)

# celery_app = Celery(
#     broker_url="amqp://guest:guest@rabbitmq_broker:5672//",
#     result_backend="redis://:TestTest12345678@redis_cache:6379/0",
#     task_serializer="json",
#     result_serializer="json",
#     accept_content=["json"],
#     include=["celery_worker.app"],
#     broker_transport_options={
#         "max_retries": 1,
#         "visibility_timeout": 365 * 24 * 60 * 60,
#     },
# )
# "--broker=amqp://guest:guest@rabbitmq_broker:5672//", "flower", "-A", "celery_worker.app", "--basic_auth=guest:guest", "--port=5555", "--broker_api=http://guest:guest@rabbitmq_broker:15672/api/vhost"
