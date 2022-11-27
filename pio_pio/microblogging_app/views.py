from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.


class PostListView(ListView):

    model = Post
    template_name = 'microblogging_app/list.html'
    context_object_name = 'posts'
    paginate_by = 20


class PostCreateView(CreateView):
    model = Post
    template_name = 'microblogging_app/form.html'
    fields = ('author', 'content')
    success_url = reverse_lazy('microblogging_app:post-list')


class PostDetailView(DetailView):

    model = Post
    template_name = 'microblogging_app/detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):

    model = Post
    template_name = 'microblogging_app/form.html'
    context_object_name = 'post'
    fields = ('content')

    def get_success_url(self):
        return reverse_lazy('microblogging_app:post-list')


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'microblogging_app/confirm_delete.html'
    success_url = reverse_lazy('microblogging_app:post-list')
