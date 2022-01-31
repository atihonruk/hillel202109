#!/bin/sh

sleep 10

echo Collect static files.
./manage.py collectstatic

echo Run database migrations.
./manage.py migrate

echo Starting Django.
gunicorn django_blog.wsgi --bind 0.0.0.0:$PORT
