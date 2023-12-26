FROM python:3.12.0-slim-bullseye
COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
WORKDIR /

# CMD celery --app celery_worker.app worker  -l info
# CMD celery -A celery_worker.app worker --loglevel=INFO --concurrency=4 -Q celery
CMD celery -A celery_worker.app worker --loglevel=INFO