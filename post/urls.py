from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create-post/', views.create_post, name='create post'),
    path('view-post/<int:post_id>/', views.view_post, name='view post'),
]