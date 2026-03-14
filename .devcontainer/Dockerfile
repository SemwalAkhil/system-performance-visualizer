FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    python3 \
    python3-venv \
    python3-pip \
    git \
    curl \
    && apt-get clean

WORKDIR /workspace