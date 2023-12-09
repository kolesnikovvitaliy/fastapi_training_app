#!/bin/sh

set -e

# activate our virtual environment here
. /${PATH_APP_IN_DOCKER}/.venv/bin/activate

# run poetry activate dependencies for save in localmaсhine
# cd /backend && poetry lock --no-update
poetry lock --no-update
cd /${PATH_APP_IN_DOCKER}/${APP_NAME}
alembic revision --autogenerate -m "init revision alembic"
alembic upgrade head
cd ..
# Evaluating passed command:
exec "$@"