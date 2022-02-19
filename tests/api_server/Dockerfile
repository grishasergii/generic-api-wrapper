FROM python:3.9-slim-buster

RUN pip install --upgrade pip
RUN pip install flask

WORKDIR app/

COPY . .

CMD flask run --host 0.0.0.0