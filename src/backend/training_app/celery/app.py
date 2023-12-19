from celery import Celery

# from .config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery(
    broker_url="amqp://guest:guest@rabbitmq_broker:5672",
    result_backend="redis://redis:TestTest12345678@redis_cache:6379/0",
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    include=["celery.worker"],
    broker_transport_options={
        "max_retries": 1,
        "visibility_timeout": 365 * 24 * 60 * 60,
    },
)
