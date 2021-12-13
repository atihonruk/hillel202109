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


def save_key():
    while True: # 100
        # if Url.objects.get(key=key).exists(): # select 10000000
        key = generate_key() 
        try:
            insert_key(key)
            return key
        except:
            pass

    return key


@login_required
def handle_post(request):
    # handle form
    form = UrlForm(request.POST or None)
    if form.is_bound and form.is_valid():
        key = generate_key()
        obj = form.save(commit=False)
        obj.user = request.user
        obl.save()
        
    
    return redirect('/')


from django.db.models import F


def handle_redirect(request, key):    
    try:
        url = Url.objects.get(key=key).url   # select url, key, redirect_count from urls where key=:key 5
        # url.redirect_count += 1              # 6
        url.redirect_count = F('redirect_count') + 1   # update urls set redirect_count = redirect_count + 1
        url.save()                           # update urls set redirect_count = 6
    except Exception: # Model.DoesNotExist
        url = '/'   # reverse
    return redirect(to=url)
