# pull official base image
FROM python:3.10.2-slim-buster

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

# set working directory
WORKDIR /opt/src

# install application dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy application
COPY . .
