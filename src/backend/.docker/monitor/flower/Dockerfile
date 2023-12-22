FROM python:3.12.0-slim-bullseye
COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install flower
WORKDIR /

CMD celery -A celery_worker.worker flower --persistent=True --basic_auth=guest:guest --port=5555
# CMD ["celery", "--broker=amqp://guest:guest@rabbitmq_broker:5672//", "flower", "--port=5555", "--broker_api=http://guest:guest@rabbitmq_broker:15672/api/", "--debug", "--persistent=True", "--state_save_interval=10000", "purge_offline_workers=10s"]
# CMD ["celery", "--broker=amqp://guest:guest@rabbitmq_broker:5672//", "flower", "-A", "celery_worker.worker", "--basic_auth=guest:guest", "--port=5555", "--broker_api=http://guest:guest@rabbitmq_broker:15672/api/vhost"]
# CMD ["celery", "--broker=amqp://guest:guest@rabbitmq_broker:5672//", "flower", "--basic_auth=guest:guest", "--port=5555", "--broker_api=http://guest:guest@rabbitmq_broker:15672/api/vhost"]