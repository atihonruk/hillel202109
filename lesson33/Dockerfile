FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --clear --ignore-pipfile
ENV DJANGO_SETTINGS_MODULE=django_blog.settings.heroku
ENTRYPOINT ["/app/docker-entrypoint.sh"]
