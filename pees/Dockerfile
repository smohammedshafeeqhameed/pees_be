# Use an official Python runtime as the base image
FROM python:3.10 as compiler

# Set the working directory
WORKDIR /app

# Installing additional packages
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc libmagic-dev && \
    apt-get clean

RUN apt-get update \
    && apt-get install -y --no-install-recommends awscli \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .


# Expose port 8000 for the Django app
EXPOSE 9090

# Start the application with uWSGI
#CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
CMD ["gunicorn", "pees.wsgi:application", "--bind", "0.0.0.0:9090"]

