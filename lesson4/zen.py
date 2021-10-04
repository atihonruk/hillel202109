from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.conf import settings

from django.shortcuts import redirect, render

import this
from random import choice
from pprint import pprint


DEBUG=True
ROOT_URLCONF=__name__
SECRET_KEY='asdf'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [''],
    }
]


text = ''.join(this.d.get(c, c) for c in this.s)
title, _, *quotes = text.splitlines()

from datetime import datetime 


def handler(request):
    ctx = {'title': title,
           'message': choice(quotes),
           'users': [(1, 'Alex'), (2, 'Marie'), (3, 'Zach')],
           'b': {'a': 1, 'b': 2},
           'c': datetime.now(),
           }
    for x in range(10):
        x * x
    
    return render(request,
                  'index.html', 
                  ctx)


urlpatterns = [
    path('', handler),
]


if __name__ == '__main__':
    execute_from_command_line()
