from celery import Celery

from .config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


class MyCelery(Celery):
    def gen_task_name(self, name, module):
        if module.endswith(".worker") and module.startswith("training_app"):
            module = module[13:]
        return super().gen_task_name(name, module)


celery_app = MyCelery(
    "app",
    # broker="amqp://guest:guest@rabbitmq_broker:5672",
    broker=CELERY_BROKER_URL,
    # backend="redis://:TestTest12345678@redis_cache:6379/1",
    backend=CELERY_RESULT_BACKEND,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    include=["celery_worker.worker"],
    broker_transport_options={
        "max_retries": 1,
        "visibility_timeout": 365 * 24 * 60 * 60,
    },
)