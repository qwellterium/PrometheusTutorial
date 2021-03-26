FROM python:3.9-slim-buster

COPY ./src /App
WORKDIR /App
RUN pip install -r requirements.txt

CMD uvicorn --host 0.0.0.0 --port 8000 main:App