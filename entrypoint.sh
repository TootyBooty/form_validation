#!/bin/bash

while ! nc -z mongodb 27017
do
  echo "Failure connected to MongoDB"
  sleep 3
done

uvicorn main:app --host 0.0.0.0 --port 8000