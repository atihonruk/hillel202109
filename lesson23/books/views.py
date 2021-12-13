from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse

from .models import Author, Book
from .autocomplete import get_completions


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'phone', 'gender']
        

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

    def clean_subject(self, val):
        return val.strip()


def create_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_bound and form.is_valid():
        user = form.save()
        user.is_staff = True
        user.save()
        return redirect('/')
    return render(request, 'register.html', {'form': form})


def index(request):
    if request.method == 'GET':
        form = AuthorForm()
    elif request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'form': form})


def logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


def autocomplete_book(request):
    word = request.GET.get('word', None)
    result = []
    if word:
        ids = get_completions(Book, 'title', word.lower())
        if ids:
            result = [{'id': pk,
                       'title': title}
                      for title, pk in ids]
    return JsonResponse(result, safe=False)
