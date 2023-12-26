import os

REDIS_USER = f'{os.environ.get("REDIS_USER")}'
REDIS_HOST = f'{os.environ.get("REDIS_HOST")}'
REDIS_PORT = int(f'{os.environ.get("REDIS_PORT")}')
REDIS_PASSWORD = f'{os.environ.get("REDIS_PASSWORD")}'
REDIS_CELERY_DB_INDEX = int(f'{os.environ.get("REDIS_CELERY_DB_INDEX")}')
REDIS_STORE_DB_INDEX = int(f'{os.environ.get("REDIS_STORE_DB_INDEX")}')

RABBITMQ_HOST = f'{os.environ.get("RABBITMQ_HOST")}'
RABBITMQ_USERNAME = f'{os.environ.get("RABBITMQ_USERNAME")}'
RABBITMQ_PASSWORD = f'{os.environ.get("RABBITMQ_PASSWORD")}'
RABBITMQ_PORT = int(f'{os.environ.get("RABBITMQ_PORT_1")}')

CELERY_BROKER_URL = f"amqp://{RABBITMQ_USERNAME}:{
    RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}"

CELERY_RESULT_BACKEND = f"redis://:{
    REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB_INDEX}"

REDIS_STORE_CONN_URI = f"redis://:{
    REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_STORE_DB_INDEX}"

stages = ["confirmed", "shipped", "in transit", "arrived", "delivered"]
STAGING_TIME = 15  # seconds