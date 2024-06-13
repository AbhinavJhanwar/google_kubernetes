FROM python:3.8
# FROM python:3-slim-buster
LABEL owner="Abhinav Jhanwar"
LABEL description="This example creates sample Dockerfile for backend."

# define working directory and create the directory in the container
ENV appDir /app
RUN mkdir -p $appDir

# Set the working directory in the container
WORKDIR ${appDir}

# Copy the current directory contents into the container at /app
COPY api.py ${appDir}
COPY requirements.txt ${appDir}

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]




