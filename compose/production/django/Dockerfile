FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /home/app/web

COPY compose/production/django/entrypoint.sh \
    back/requirements/base.txt \
    back/requirements/production.txt  /

RUN    mkdir /home/app/static \
    && mkdir /home/app/media \
    && mkdir /home/app/import_files \
    && mkdir /home/app/logs \
    && pip install -U pip \
    && pip install -r /production.txt \
    && rm /base.txt \
    && rm /production.txt 

ADD ./back /home/app/web

RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]