FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --clear --ignore-pipfile
ENV DJANGO_SETTINGS_MODULE=zen
CMD ["python3", "zen.py", "runserver", "0.0.0.0:8000"]

