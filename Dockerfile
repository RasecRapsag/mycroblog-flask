FROM python:3.8-alpine

RUN adduser -D mycroblog

WORKDIR /home/mycroblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY mycroblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP mycroblog.py

RUN chown -R mycroblog:mycroblog ./
USER mycroblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
