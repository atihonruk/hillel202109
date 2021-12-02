import os
from celery import Celery

# 1. configuration module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_task_runner.settings')

# 2. Celery application
app = Celery('django_task_runner')


# 3. Object and namespace
app.config_from_object('django.conf:settings',
                       namespace='CELERY')

# 4. Autodiscover tasks marked by shared_task
app.autodiscover_tasks()
