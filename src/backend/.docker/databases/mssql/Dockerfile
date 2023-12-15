FROM mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04
# FROM mcr.microsoft.com/mssql/server:2022-latest

ENV APP_DIR=/opt/app

USER root

RUN groupadd --gid 1000 userapp \
    && useradd --uid 1000 --gid userapp --shell /bin/bash --create-home userapp

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR
RUN touch config.log && chown userapp config.log
COPY ./scripts scripts
COPY ./config config

RUN chmod +x ./scripts/init-db-run.sh \
    && chmod +x ./scripts/entrypoint.sh

EXPOSE 1433

USER mssql

CMD /bin/bash $APP_DIR/scripts/entrypoint.sh