# Use the official Python image from the Docker Hub
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ../server/requirements.txt requirements.txt

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the server folder into the container
COPY ../server /app

ENV PYTHONPATH=/app

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Specify the command to run on container start
CMD ["python", "run.py"]
