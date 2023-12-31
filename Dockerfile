FROM python:3.9

ENV PYTHONWRITEBYCODE 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . /app