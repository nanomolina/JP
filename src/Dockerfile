FROM python:2.7-alpine
MAINTAINER Pdental ltda

ENV PYTHONUNBUFFERED 1

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev

COPY ./odontology/requirements.txt ./docker_app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./docker_app/requirements.txt

EXPOSE 8000
WORKDIR /odontology
ADD . /odontology

CMD ["python", "--version"]

#RUN adduser -D user
#USER user
