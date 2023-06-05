FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./manage.py ./
COPY ./config ./config
COPY ./shop ./shop
# COPY ./static ./static

RUN python manage.py migrate
RUN python manage.py collectstatic
