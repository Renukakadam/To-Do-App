# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install required packages
RUN pip install flask flask-cors

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
