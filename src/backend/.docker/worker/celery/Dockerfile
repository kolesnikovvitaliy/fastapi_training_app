FROM python:3.12.0-slim-bullseye
COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

WORKDIR /celery

CMD celery --app app worker  -l info