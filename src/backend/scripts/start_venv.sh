#!/bin/sh

set -e

# activate our virtual environment here
. /backend/.venv/bin/activate

# You can put other setup logic here
cd /backend && poetry lock
# Evaluating passed command:
exec "$@"