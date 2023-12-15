#!/bin/sh
DOCKER_DATA_BACKEND_PATH='./.docker_data'
docker-compose -f ./src/docker-compose.dev.yml down -v & disown
PPPID=$(awk '{print $4}' "/proc/$PPID/stat")
sleep 50 &&
chmod +x ./scripts/rm_docker_tmp_files.sh \
    && ./scripts/rm_docker_tmp_files.sh 
kill $PPPID
