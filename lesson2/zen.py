from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.conf import settings

import this
from random import choice

# URL
# https://docs.python.org # /3/library/index.html path

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
)


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


def handler(request):
    return HttpResponse(TEMPLATE.format(title=title,
                                        message=choice(quotes)))


urlpatterns = [
    path('', handler)
]


if __name__ == '__main__':
    execute_from_command_line()
