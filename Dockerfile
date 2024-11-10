# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt and install packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's code to the working directory
COPY . .

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
