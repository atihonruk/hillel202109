import dj_database_url
from .common import *

DEBUG = False

ALLOWED_HOSTS = ['gentle-eyrie-55804.herokuapp.com']

DATABASES['default'] = dj_database_url.config()
