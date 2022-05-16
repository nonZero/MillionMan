from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from rest_framework.viewsets import ModelViewSet

from .models import Post
from . import forms
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(ListView):
    model = Post
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    success_message = "Post created."
    permission_required = "expenses.add_post"


class PostUpdateView(UpdateView):
    model = Post
    form_class = forms.PostForm


class PostDeleteView(DeleteView):
    success_url = reverse_lazy("posts:list")
