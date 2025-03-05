#FROM ubuntu:latest
#LABEL authors="dave.jamison"
#
#ENTRYPOINT ["top", "-b"]

# Use an official Python runtime as a parent image #
FROM python:3.12.9-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GCRYPT_IN_HW_RNG=0 \
    APPLICATION_ABBREVIATION="PDFViewer" \
    APPLICATION_NAME="PDF Viewer"

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev python3-dev \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Collect static files
# Adjust this if you have a custom location for static files
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "django_project.wsgi:application"]