FROM python:3.9-slim
WORKDIR /app
COPY . .
ENTRYPOINT ["/app/docker-entrypoint.sh"]
RUN pip install pipenv
RUN pipenv install --system --deploy --clear --ignore-pipfile
ENV DJANGO_SETTINGS_MODULE=django_blog.settings.heroku
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
