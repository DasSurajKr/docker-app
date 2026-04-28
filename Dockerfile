# Use an official Python base image
FROM python:3.11-slim
# Set the working directory
WORKDIR /app
# Copy dependency file first (for caching)
COPY requirements.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the app
COPY . .
# Expose the container port
EXPOSE 5000
# Run the Flask app
CMD ["python", "app.py"]