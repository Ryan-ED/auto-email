# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY . .

# Run send_email.py when the container launches
CMD ["python", "auto_email.py"]
