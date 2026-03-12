# Base dev container image
FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install system dependencies required for the project
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    python3 \
    python3-venv \
    python3-pip \
    git \
    curl \
    && apt-get clean

# Set working directory
WORKDIR /workspace

# Copy backend requirements file into container
COPY backend/requirements.txt /tmp/requirements.txt

# Create Python virtual environment
RUN python3 -m venv /workspace/.venv

# Install Python dependencies inside virtual environment
RUN /workspace/.venv/bin/pip install --upgrade pip && \
    /workspace/.venv/bin/pip install -r /tmp/requirements.txt

# Ensure the virtual environment is activated automatically
ENV PATH="/workspace/.venv/bin:$PATH"