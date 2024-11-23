from django.views import generic

from Blog.forms import PostForm, CreatePostForm
from Blog.models import Posts


class PostListView(generic.ListView):
    model = Posts


class PostDetailView(generic.DetailView):
    model = Posts


class PostCreateView(generic.CreateView):
    model = Posts
    form_class = CreatePostForm


class PostUpdateView(generic.UpdateView):
    model = Posts


class PostDeleteView(generic.DeleteView):
    model = Posts


