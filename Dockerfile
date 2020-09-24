FROM python:3.8-alpine
LABEL maintainer "Matias Estevez"

COPY . /compragamer
WORKDIR /compragamer

RUN pip install pipenv && pipenv install --deploy
ENTRYPOINT ["pipenv", "run"]
