FROM python:3.9.8-alpine3.14

COPY ./src /app

WORKDIR /app

RUN ls -ltr

RUN pip install -r requirements.txt

EXPOSE 5005

ENTRYPOINT python pythonapp.py