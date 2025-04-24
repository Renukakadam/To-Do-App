# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first to leverage caching
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the Flask port (for documentation)
EXPOSE 5000

# Run the application with proper host binding
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "5000"]
