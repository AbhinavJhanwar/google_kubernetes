FROM python:3.8
LABEL owner="Abhinav Jhanwar"
LABEL description="This example creates sample Dockerfile for frotend."

# define working directory and create the directory in the container
ENV appDir /app/frontend
RUN mkdir -p $appDir

# Set the working directory in the container
WORKDIR ${appDir}

# Copy the current directory contents into the container at /app
COPY user_interface.py ${appDir}
COPY requirements.txt ${appDir}

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "user_interface.py"]



