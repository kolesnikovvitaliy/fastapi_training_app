#!/bin/sh
chmod +x ./scripts/create_docker_tmp_files.sh \
    && ./scripts/create_docker_tmp_files.sh && \
cd src
docker-compose -f docker-compose.dev.yml up --remove-orphans --build
