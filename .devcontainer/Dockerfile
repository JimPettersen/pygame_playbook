FROM python:3.10-slim

# Install necessary tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Pygame
RUN pip install pygame
