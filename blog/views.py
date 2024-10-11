from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class HomeView(generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

class LatestPostsView(generic.ListView):
    template_name = 'blog/latest_posts.html'
    context_object_name = 'recent_posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:10]


class CategoryPostsView(generic.ListView):
    template_name = 'blog/category_posts.html'
    context_object_name = 'category_posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug'))

