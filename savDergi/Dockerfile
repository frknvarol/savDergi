FROM python:3.12.2

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /app/
RUN python3 -m pip install --no-cache-dir -r requirements.txt


COPY . /app/