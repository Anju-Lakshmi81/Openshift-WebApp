# Use official Python 3.11 image based on UBI8 for compatibility with OpenShift
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose the port your Flask app runs on
EXPOSE 8080

# Use environment variable for the Flask port (OpenShift provides PORT)
ENV PORT=8080

# Run the application
CMD ["python", "app.py"]

