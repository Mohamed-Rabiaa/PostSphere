from django.conf import settings
from blog import models

def media_url(request):
    context = {}
    views_list = ['home', 'latest_posts', 'category', 'profile', 'post_detail']
    current_view = request.resolver_match.view_name if request.resolver_match else None
    if current_view in views_list:
        context['MEDIA_URL'] = settings.MEDIA_URL
    return context

def get_categories(request):
    context = {}
    views_list = ['home', 'latest_posts', 'category']
    current_view = request.resolver_match.view_name if request.resolver_match else None
    if current_view in views_list:
        categories = models.Category.objects.order_by('slug').all()
        context['categories'] = categories
    return context

def get_nav_objects(request):
    context = {}
    current_view = request.resolver_match.view_name if request.resolver_match else None
    no_header_views = ['login', 'register']

    if current_view not in no_header_views:
        nav_objects = [
            {'nav_view_name': 'home', 'nav_link_text': 'Home'},
            {'nav_view_name': 'new_post', 'nav_link_text': 'New Post'},
            {'nav_view_name': 'profile', 'nav_link_text': 'Profile'},
            {'nav_view_name': 'logout', 'nav_link_text': 'Logout'},
        ]
        context['nav_objects'] = nav_objects
    return context
