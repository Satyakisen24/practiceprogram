# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Create a non-root user
Run useradd -m appuser

# Copy project files into the container
COPY . ./

# Install any dependencies specified in the requirements file
User appuser

# Run the Python script
CMD ["python3", "report.py"]