from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Post
from .forms import NewPostForm

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

@login_required
def new_post_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # Don't save to the database yet
            post.author = request.user # Set the author to the current logged-in user
            post.save() # Now save to the database
            return redirect('home')
    else:
        form = NewPostForm()

    return render(request, 'blog/new_post.html', {'form': form})
