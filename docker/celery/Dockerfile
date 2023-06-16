# Use an official Python runtime as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
# WORKDIR /app
WORKDIR /app/src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /app

# Run the Celery worker
CMD celery -A src.config.celery worker --loglevel=info
