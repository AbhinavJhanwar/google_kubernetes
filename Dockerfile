FROM python:3.8
LABEL owner="Abhinav Jhanwar"
LABEL description="This example creates sample Dockerfile."

# define working directory and create the directory in the container
ENV appDir /app
RUN mkdir -p $appDir

# Set the working directory in the container
WORKDIR ${appDir}

# Copy the current directory contents into the container at /app
COPY main.py ${appDir}
COPY requirements.txt ${appDir}

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

CMD ["python", "main.py"]



