FROM debian:bullseye-20231120

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y redis-server=5:${REDIS_VERSION}* \
    && rm -rf /var/lib/apt/lists/*

COPY ./config/redis.conf /etc/redis/redis.conf
COPY ./scripts/entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 6379/tcp
ENTRYPOINT ["/sbin/entrypoint.sh"]

