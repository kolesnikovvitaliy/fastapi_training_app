import os


REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_CELERY_DB_INDEX = os.environ.get("REDIS_CELERY_DB_INDEX")
REDIS_STORE_DB_INDEX = os.environ.get("REDIS_STORE_DB_INDEX")

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
RABBITMQ_USERNAME = os.environ.get("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD")
RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT")

CELERY_BROKER_URL = "amqp://appuser:TestTest12345678@rabbitmq_broker:5672"
CELERY_RESULT_BACKEND = "redis://:TestTest12345678@redis_cache:6379/0"
REDIS_STORE_CONN_URI = "redis://:TestTest12345678@redis_cache:6379/0"
stages = ["confirmed", "shipped", "in transit", "arrived", "delivered"]
STAGING_TIME = 15  # seconds
