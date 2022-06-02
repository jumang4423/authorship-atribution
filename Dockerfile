FROM --platform=arm64 python:3
COPY . /el331
WORKDIR /el331

RUN apt-get update
RUN apt-get -y install build-essential