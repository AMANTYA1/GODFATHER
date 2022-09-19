FROM debian:11
FROM python:3.10.1-slim-buster

WORKDIR /TGN/

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install git
RUN python3.9 -m pip install -U pip
RUN apt-get install -y wget python3-pip curl bash neofetch ffmpeg software-properties-common
RUN apt-get install git curl python3-pip ffmpeg -y
RUN python3 -m pip install --upgrade pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY . /app/
WORKDIR /app/

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

COPY . .
CMD ["python3.9", "-m", "TGN"]
