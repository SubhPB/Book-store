
#  base image
FROM python:3.9

# This env variable will ensures that python will not try to write .pyc files which we do not need.
ENV PYTHONDONTWRITEBYTECODE 1

# THE FOLLOWING : will ensures that console output looks familiar and is not buffered by Docker
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# install dependencies..

# COPY 1st_dep 2nd_dep  where to copy
# do you remember, these fles were formed after running pipenv install django...
COPY Pipfile Pipfile.lock /code/


RUN pip install pipenv && pipenv install --system


# copy project 
COPY . /code/

