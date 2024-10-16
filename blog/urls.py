from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/latest_posts/', views.LatestPostsView.as_view(), name='latest_posts'),
    path('home/<slug:slug>/', views.CategoryPostsView.as_view(), name='category'),
    path('home/post_details/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new_post/', views.new_post_view, name='new_post'),
    path('post_update/<slug:slug>/', views.update_post_view, name='post_update'),
    path('post_delete/<slug:slug>/', views.delete_post_view, name='post_delete'),
]
