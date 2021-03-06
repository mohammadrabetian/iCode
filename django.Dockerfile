# pull official base image
FROM python:3.8.0-alpine

LABEL maintainer="Mohammad Rabetian <mohammadrabetian@gmail.com>"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# make directory & install dependencies
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /code/entrypoint.sh

# copy project
COPY . /code/

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
