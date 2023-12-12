#!/bin/sh
docker-compose -f ./src/docker-compose.dev.yml down -v & disown
PPPID=$(awk '{print $4}' "/proc/$PPID/stat")
sleep 35
kill $PPPID


