"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views
from books import views as book_views

urlpatterns = [
    path('get-completions', book_views.autocomplete_book), # GET ?a=1,b=2

    #    path('', views.handle_url),
    path('<key>', views.handle_redirect),
    path('admin/', admin.site.urls),
    path('', book_views.index),

    # API
    # CRUD, REST-style, django-rest-framework
    # path('book/<pk>', ...),  # unique object, DELETE, PATCH/POST
    # path('book/create', ...), # POST (PUT)
    # path('book/list'), # GET

    # RPC
    # path('doCreate', ...),
    # path('placeOrder', ...),

]
