#base image
FROM python:3.9

#it doesn't write file .pyc
ENV PYTHONDONTEBYTECODE 1 
#the output will be familiar to us
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /book_store/

#Install dependencies
COPY Pipfile Pipfile.lock /book_store/
RUN pip3 install pipenv && pipenv install --system

COPY . /book_store/