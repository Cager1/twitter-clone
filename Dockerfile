# Use an official Python runtime as a parent image
FROM arm64v8/python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy all contents from the current directory into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
