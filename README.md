# Event REST_API
REST_API information about events

## Goals
Understand how to work with databases, requests, http protocol. Also docker, dockerfile, docker-compose

## To run
In order to run it, you will need to download a list of Python modules(in requirement.txt). You should enter commands in the terminal:

    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver {host}:{port}

## To run in docker
    docker-compose up --build
