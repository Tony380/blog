from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
DetailView, 
CreateView, 
DeleteView, 
UpdateView,
View)
from .models import Post, User


class DisplayUserPosts(ListView):
    model = Post
    template_name = 'home/display.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class index(ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class Detail(DetailView):
    model = Post


class Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class Create(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'home/about.html')


def my_404_view(request, exception):
    """ Error 404 page """
    return render(request, '404.html')


def my_500_view(request):
    """ Error 500 page """
    return render(request, '500.html')