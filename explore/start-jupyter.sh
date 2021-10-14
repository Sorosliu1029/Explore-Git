#!/bin/env bash
docker run \
    -d \
    -p 8888:8888 \
    -v "${PWD}/..":/home/jovyan \
    -v /tmp:/tmp \
    jupyter/minimal-notebook:latest \
    start-notebook.sh --NotebookApp.password='sha1:34147a04de8e:28b0c1d0c034adf65f78074e69253c7f83e18144'
