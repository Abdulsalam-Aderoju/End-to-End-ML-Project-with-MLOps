# Use the Python 3.8 slim-buster image as the base image
FROM python:3.8-slim-buster


# Update the package list and install AWS CLI
RUN apt update -y && apt install awscli -y


# Set the working directory inside the container to /app
WORKDIR /app


# Copy the current directory contents into the container at /app
COPY . /app


# Install the dependencies listed in requirements.txt (we can use pip since we already made python the base image)
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Run the app using Python 3
CMD ["python", "app.py"]

