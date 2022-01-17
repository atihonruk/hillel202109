from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Post


class PostDetail(DetailView):
    model = Post


class PostList(ListView):
    model = Post

# Вам понадобятся страницы для создания поста (CreateView), редактирования (UpdateView) и удаления (DeleteView) поста.




# Естественно, редактировать и удалять можно только свои посты.

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post

    def form_valid(self, form):
        # Post()
        form.instance.created_by = self.request.user
        return super().form_valid(form)
        
# Также каждому пользователю должна быть доступна страница со списком (ListView) своих (и только своих) постов.
class PostUserList(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset() # .all()
        return qs.filter(created_by=self.request.user)


class UpdatePost(UserPassesTestMixin, UpdateView):
    def test_func(self):
        post = self.get_object()
        return post.created_by == self.request.user


def readiness(request):
    # dummy_sql = 'select 1 from limit 1'
    responses = {'postgresql': 'ready',
                 'redis': 'ready'}
    
    return HttpResponse('OK', content_type='text/plain')
