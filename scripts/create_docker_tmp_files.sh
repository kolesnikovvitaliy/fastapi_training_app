#!/bin/sh

DOCKER_DATA_BACKEND_PATH='./.docker_data'
if [ -e "$DOCKER_DATA_BACKEND_PATH" ]; then
    echo "$DOCKER_DATA_BACKEND_PATH exists."
else mkdir -p $DOCKER_DATA_BACKEND_PATH/backend \
        && cd $DOCKER_DATA_BACKEND_PATH/backend \
        && mkdir -p \
        mssql_data \
        mssql_data/data \
        mssql_data/logs \
        .venv \
        alembic_data/versions \
        redis_data \
        redis_data/data \
        redis_data/logs \
        rabbitmq_data \
        && touch ./mssql_data/logs/mssql.log \
        ./redis_data/logs/redis-server.log \
        && cd ../.. \
        && sudo chown -R 10001:0 $DOCKER_DATA_BACKEND_PATH
fi
