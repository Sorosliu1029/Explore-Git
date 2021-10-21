#!/bin/env bash

PORT=8888

docker run \
    -d \
    -p $PORT:8888 \
    -v "${PWD}":/home/jovyan \
    -v /tmp:/tmp \
    -e NB_UID=1000 \
    -e NB_GID=1000 \
    --user root \
    ghcr.io/sorosliu1029/explore-git:latest \
    start-notebook.sh --NotebookApp.password='sha1:34147a04de8e:28b0c1d0c034adf65f78074e69253c7f83e18144'

echo "Visit localhost:${PORT} to explore Git"
