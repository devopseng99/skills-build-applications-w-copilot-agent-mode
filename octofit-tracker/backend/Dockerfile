FROM python:3.12-slim

WORKDIR /code

# Install build dependencies and postgresql client
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Create static files directory
RUN mkdir -p /code/staticfiles

# Static files will be collected at runtime with proper environment variables

EXPOSE 8000