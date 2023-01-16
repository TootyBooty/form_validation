FROM python:3.10 as requirements-stage

WORKDIR /tmp
 
RUN pip install poetry
 
COPY ./pyproject.toml ./poetry.lock* /tmp/
 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

 
FROM python:3.10
 
WORKDIR /code/app
 
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get update && apt-get -y dist-upgrade

RUN apt install -y netcat

COPY entrypoint.sh /code/app/entrypoint.sh

RUN chmod +x entrypoint.sh
 
COPY ./ /code/app

