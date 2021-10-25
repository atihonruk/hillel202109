from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.conf import settings

from django.shortcuts import redirect, render

import this
from random import choice

# URL
# https://docs.python.org # /3/library/index.html path

# settings.configure(
DEBUG=True
ROOT_URLCONF=__name__
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postrgesql',
        'NAME': 'django_start',
        'HOST': 'db',
        'PORT': 5432,
        'USER': 'django_dev',
        'PASSWORD': "asdl5iw49",
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379',
    }
}
# )


text = ''.join(this.d.get(c, c) for c in this.s)
title, _, *quotes = text.splitlines()


TEMPLATE = """
<!DOCTYPE html>
<html>
 <head>
  <title>{title}</title>
 </head>
 <body>
  <h1>{message}</h1>
 </body>
</html>
"""

from pprint import pprint

def handler(request):
    print(request.method)
    print(request.path_info)
    pprint(request.META)
    pprint(request.GET)
    pprint(request.POST)
    pprint(request.headers)

    # Accept: */*
    # HTTP_ACCEPT
    
    return HttpResponse(TEMPLATE.format(title=title,
                                        message=choice(quotes)))

    # return HttpResponse('Hello, world', content_type='application/json')
    # return HttpResponseNotFound()
    # return HttpResponse(status=404)

    return redirect('/')


def mod_handler(request, mod_name):
    pass


def obj_handler(request, mod_name, obj_name):
    pass
    

urlpatterns = [
    # http://example.com/
    path('', handler),
    # http://example.com/doc/math
    path('doc/<mod_name>', mod_handler),
    # http://example.com/doc/math/sin
    path('doc/<mod_name>/<obj_name>', obj_handler),
    # http://example.com/post/<slug>

    # http://example.com/user/1
    # path('user/<id>')
    
    
]


if __name__ == '__main__':
    execute_from_command_line()
