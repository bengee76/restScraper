FROM alpine:latest

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add python3 python3 py3-pip

WORKDIR /app

COPY requirements.txt /app/

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt

COPY . /app/
CMD [ "/opt/venv/bin/python", "flaskPage/app.py" ]