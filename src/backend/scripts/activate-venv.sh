#!/bin/sh

set -e

# activate our virtual environment here
. /backend/.venv/bin/activate

# run poetry activate dependencies for save in localmaсhine
cd /backend && poetry lock --no-update
# Evaluating passed command:
exec "$@"