FROM postgres:9.6.23
USER root
MAINTAINER ITO Manaki <iam@colk.dev>

ENV LC_ALL=en_US.UTF-8 \
    TZ=JST-9 \
    TERM=xtermdocker-attachingdocker-attaching

COPY ./docker/postgres/initdb /docker-entrypoint-initdb.d
