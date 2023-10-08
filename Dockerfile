FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY src/ /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt
