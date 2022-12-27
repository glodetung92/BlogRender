from django.shortcuts import render
from .models import Post
from django.views import generic
from django.http import HttpResponse
from django.views.decorators.http import require_GET


class postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'
    paginate_by = 3
    context_object_name = 'posts_list'


class postdetail(generic.DetailView):
    model = Post
    template_name = 'blog/page.html'
