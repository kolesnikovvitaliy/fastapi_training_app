FROM mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04
# FROM mcr.microsoft.com/mssql/server:2022-latest

ENV APP_DIR=/opt/app

USER root

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR
RUN touch config.log && chown mssql config.log
COPY ./scripts scripts
COPY ./entrypoint.sh entrypoint.sh

RUN chmod +x ./scripts/init-db-run.sh \
    && chmod +x ./entrypoint.sh

EXPOSE 1433

USER mssql

CMD /bin/bash $APP_DIR/entrypoint.sh