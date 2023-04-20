FROM python:3.9-slim-buster

RUN apt update && apt install -y pipenv 

ENV PORT=9090
WORKDIR /usr/app

COPY Pipfile .
COPY .env .
RUN pipenv --python 3.9
RUN pipenv install

COPY ./src ./src

EXPOSE ${PORT}

CMD ["pipenv","run","flask","run"] 