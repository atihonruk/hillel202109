from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView, DetailView, ListView

from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'phone', 'gender']
        

def create_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_bound and form.is_valid():
        user = form.save()
        user.is_staff = True
        user.save()
        return redirect('/')
    return render(request, 'register.html', {'form': form})


@login_required
def index(request):
    if request.method == 'GET':
        form = AuthorForm()
    elif request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'form': form})


class CreateAuthorView(CreateView):
    model = Author
    fields = ['name', 'email', 'phone', 'gender']
    template_name = 'create_author.html'
    success_url = '/'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_details.html'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'


# iv = IndexView()
# iv.run()    # MRO


# CRUD


def logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')

