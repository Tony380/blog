from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class index(ListView):

    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'
