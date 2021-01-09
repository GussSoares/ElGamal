FROM python:3.8.5

RUN mkdir /home/project/
WORKDIR /home/project/

COPY docs docs

RUN pip install -r docs/requirements.txt
