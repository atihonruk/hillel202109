#!/bin/sh

sleep 10


echo Run database migrations.
python ./manage.py migrate

echo Starting Django.
gunicorn django_blog.wsgi --bind 0.0.0.0:$PORT
