#!/bin/sh
cd src
docker-compose -f docker-compose.dev.yml up --remove-orphans --build
