FROM jupyter/minimal-notebook:ubuntu-20.04
LABEL author="Soros Liu"
LABEL org.opencontainers.image.source https://github.com/Sorosliu1029/Explore-Git

USER root

RUN apt-get update && apt-get install -y \
    tree && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}