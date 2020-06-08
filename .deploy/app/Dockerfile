FROM python:3.8-slim

ARG BUILD_PACKAGES="gcc g++ software-properties-common apt-transport-https apt-utils gnupg1 libcurl4-openssl-dev libssl-dev git-core"
ARG BUILD_DEPS="netcat ca-certificates"

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIPENV_HIDE_EMOJIS=true \
    PIPENV_COLORBLIND=true \
    PIPENV_NOSPIN=true \
    PIPENV_DOTENV_LOCATION=.env \
    DJANGO_SETTINGS_MODULE=quantum_web.settings

RUN set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends $BUILD_PACKAGES && \
    rm -rf /var/lib/apt/lists/*

RUN set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends $BUILD_DEPS && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY .deploy/app/docker-entrypoint.sh /docker-entrypoint.sh
COPY requirements.txt ./

RUN set -ex && \
    pip3 install -r requirements.txt && \
    rm -rf /usr/src/python && \
    apt-get autoremove -y && \
    chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
