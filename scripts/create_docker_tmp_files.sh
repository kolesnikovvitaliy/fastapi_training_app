#!/bin/sh

DOCKER_DATA_BACKEND_PATH='./.docker_data'
if [ -e "$DOCKER_DATA_BACKEND_PATH" ]; then
    echo "$DOCKER_DATA_BACKEND_PATH exists."
else mkdir -p $DOCKER_DATA_BACKEND_PATH/backend \
        && cd $DOCKER_DATA_BACKEND_PATH/backend \
        && mkdir -p mssql_data .venv alembic/versions \
        && touch config_mssql.log \
        && cd ../.. \
        && sudo chown -R 10001:0 $DOCKER_DATA_BACKEND_PATH
fi
