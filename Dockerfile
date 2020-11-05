FROM node:15.0.1-alpine3.10 AS static-assets

WORKDIR /code/hgapp
COPY hgapp/package.json .
RUN npm install

COPY . /code
RUN npm run build


FROM python:3.9.0-alpine3.12 AS final

WORKDIR /code/hgapp
COPY hgapp/requirements.txt .

# build dependencies
RUN set -ex && \
    apk update && \
    apk add -t virtual \
        build-base \
        libffi-dev \
        libjpeg-turbo-dev \
        postgresql-dev \
        zlib-dev \
        && \
    pip install -r requirements.txt && \
    apk del virtual

# runtime dependencies
RUN set -ex && \
    apk add \
        libjpeg-turbo \
        zlib

COPY . /code

ENV STATIC_DIR=/code/static
COPY --from=static-assets /code/hgapp/static/ ${STATIC_DIR}

ENTRYPOINT ["/usr/local/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]