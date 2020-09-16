FROM python:3.6-alpine

ENV FLASK_APP=app.py

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "flask", "run", "--host=0.0.0.0"]