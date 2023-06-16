# Use an official Python runtime as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /app

# Expose the Django app port
EXPOSE 8000

# Run migrations and start the Django app
CMD python3 src/manage.py migrate && python3 src/manage.py runserver 0.0.0.0:8000
