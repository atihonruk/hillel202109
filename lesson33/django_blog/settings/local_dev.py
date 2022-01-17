from .common import *

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db',
        'NAME': 'django_start',
        'USER': 'django_dev',
        'PASSWORD': 'asdl5iw49',
        'PORT': 5432,
    }
}
