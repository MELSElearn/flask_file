FROM python:3.8-slim

WORKDIR /app

COPY . ./

RUN pip install flask gunicorn CurrencyConverter opencv-python-headless Pillow pybase64 numpy

CMD gunicorn --bind :$PORT app:app
