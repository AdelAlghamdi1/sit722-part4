# Use an official Python image as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables for the database connection (Update this if needed)
ENV DATABASE_URL=postgresql://deakinlab8_2_user:GPSSjl4x1smhSNzdiEXIU7i0mwfJDf10@dpg-crinp4lumphs73cndcng-a.oregon-postgres.render.com/deakinlab8_2

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]