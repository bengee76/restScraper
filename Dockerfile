FROM alpine:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN apk update && apk add python3 py3-pip chromium-chromedriver chromium bash xvfb

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt

CMD [ "sh", "runScraper.sh" ]
