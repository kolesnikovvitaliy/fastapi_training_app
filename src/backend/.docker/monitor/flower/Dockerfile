FROM python:3.12.0-slim-bullseye
COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install flower
WORKDIR /


CMD celery -A celery_worker.app flower --basic_auth=${RABBITMQ_USERNAME}:${RABBITMQ_PASSWORD} --port=${FLOWER_CELERY_PORT} --broker_api=${RABBITMQ_BROKER_API} --purge_offline_workers=10
############################
# CMD ["celery", "--broker=amqp://guest:guest@rabbitmq_broker:5672//", "flower", "--basic_auth=guest:guest", "--port=5555", "--broker_api=http://guest:guest@rabbitmq_broker:15672/api/vhost", "--persistent=True", "--state_save_interval=10000", "--purge_offline_workers=10"]
#############################
