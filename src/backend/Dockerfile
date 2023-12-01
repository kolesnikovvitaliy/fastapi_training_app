###############################################
# Base Image
###############################################
FROM python:3.12.0-slim-bullseye AS python-base
ENV PYTHONUNBUFFERED=1 \
    PROJECT_NAME="trainig_app" \
    WORKDIR_PROJECT="/backend" \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.0  \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/backend" \
    VENV_PATH="/backend/.venv" \
    MSSQL_ODBC_DATASOURCES="/etc/ODBCDataSources" \
    MSSQL_ODBC_INI="/etc/odbc.ini" \
    MSSQL_ODBC_INT="/etc/odbcinst.ini" \
    MSSQL_DRIVER="/opt/mssql-tools18" \
    MSSQL_MICROSOFT="/opt/microsoft" 

# prepend poetry, venv and mssql to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$MSSQL_DRIVER/bin:$PATH"

###############################################
# Builder VENV_POETRY
###############################################
FROM python-base as builder-poetry
RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -yq curl \ 
    && apt-get install -yq --no-install-recommends $buildDeps 

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} && \
    chmod a+x /opt/poetry/bin/poetry \
    && rm -rf ~/.cache/pypoetry/{cache,artifacts}


# We copy our Python requirements here to cache them
# and install only runtime deps using poetry

WORKDIR $PYSETUP_PATH
COPY ./pyproject.toml ./
RUN poetry lock --no-update
RUN poetry install --only main --no-root --no-cache # respects \ 
    && rm -rf ~/.cache/pypoetry/{cache,artifacts} \
    && apt-get clean \
    && apt-get purge -y --auto-remove \ 
    && rm -rf /var/lib/apt/lists/*

###############################################
# Build MSSQL-DRIVER
###############################################
FROM python-base as builder-mssql-driver
RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -yq \
    curl \
    apt-transport-https \
    debconf-utils \
    gnupg2 \
    && apt-get install -yq --no-install-recommends $buildDeps 

# Install mssql-tools18, msodbcsql18 $MSSQL_DRIVER, $MSSQL_MICROSOFT
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc \
    && curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql18 \
    mssql-tools18 \
    && apt-get clean \
    && apt-get purge -y --auto-remove \ 
    && rm -rf /var/lib/apt/lists/*

###############################################
# Production Image
###############################################
FROM python-base as production

LABEL maintainer="kolesnikovvitaliy <kolesnikovvitaliy@github.com>"

# Copying mssql-driver config and poetry-venv into image
COPY --from=builder-poetry $POETRY_HOME $POETRY_HOME
COPY --from=builder-poetry $PYSETUP_PATH $PYSETUP_PATH
COPY --from=builder-mssql-driver $MSSQL_DRIVER $MSSQL_DRIVER
COPY --from=builder-mssql-driver $MSSQL_MICROSOFT $MSSQL_MICROSOFT
COPY --from=builder-mssql-driver $MSSQL_ODBC_DATASOURCES $MSSQL_ODBC_DATASOURCES
COPY --from=builder-mssql-driver $MSSQL_ODBC_INT $MSSQL_ODBC_INT
COPY --from=builder-mssql-driver $MSSQL_ODBC_INI $MSSQL_ODBC_INI


SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc \
    && source ~/.bashrc 

# and install unixodbc-dev for connect mssql
RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    apt-utils \
    gcc \
    && apt-get update \
    && apt-get install -yq --no-install-recommends unixodbc-dev \
    && apt-get clean \
    && apt-get purge -y --auto-remove \ 
    && rm -rf /var/lib/apt/lists/*

# create worcdir
# poetry install dependens
WORKDIR $WORKDIR_PROJECT
RUN poetry lock --no-update
RUN poetry install --no-root --no-cache \
    && rm -rf ~/.cache/pypoetry/{cache,artifacts} \
    && apt-get clean \
    && apt-get purge -y --auto-remove \ 
    && rm -rf /var/lib/apt/lists/*

COPY ./scripts scripts
COPY ./training_app training_app
COPY ./tests tests
COPY ./main.py main.py

RUN chmod +x ./scripts/start_venv.sh

EXPOSE 8000

# start activate venv for training_app
ENTRYPOINT $WORKDIR_PROJECT/scripts/start_venv.sh $0 $@

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /backend
USER appuser


# CMD ["uvicorn", "--reload", "training_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "main.py"]