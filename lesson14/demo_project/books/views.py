from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import CreateView, DetailView, ListView
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'phone', 'gender']


class ContactForm(forms.Form):
    user = forms.CharField()
    message = forms.CharField()
    

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


class CreateAuthorFormView(View):
    # dispatch

    def get(self, request):
        form = AuthorForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'index.html', {'form': form})


class CreateAuthorView(LoginRequiredMixin, CreateView):
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
    paginate_by = 2


# iv = IndexView()
# iv.run()    # MRO


# CRUD
class AuthorBooksView(SingleObjectMixin, ListView):
    template_name = 'author_books.html'

    # NB: get_queryset - conflict!

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.book_set.all()


def logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


class ContactFormMixin:
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)  # !!!
        ctx['contact_form'] = ContactForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return super().post(request, *args, **kwargs)
    
