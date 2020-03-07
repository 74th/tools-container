FROM ubuntu:rolling

RUN apt-get update && \
    apt-get install -y \
    git \
    curl && \
    apt-get autoremove