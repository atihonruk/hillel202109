import random
# from urllib.parse import urlsplit

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db import models

from .models import Url

from django.contrib.auth.decorators import login_required

# def handle_url(request):
#     url = request.PATH.get('url')
    
#     if urlsplit(url).scheme in {'http', 'https', 'ftp'}:
#         key = gen_key()
#         cache.set(key, url)
#         return redirect('/')
    
    

# def handle_redirect(request, key):
#    return redirect(cache.get(key, '/'))


class IndexView(TemplateView):
    template_name = 'index.html'


def index(request):
    return HttpResponse('Hello')


@login_required
def handle_post(request):
    # handle form
    return redirect('/')


def handle_redirect(request, key):
    try:
        url = Url.objects.get(key=key).url
    except Exception: # Model.DoesNotExist
        url = '/'   # reverse
    return redirect(to=url)
