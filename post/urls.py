from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create-post/', views.create_post, name='create post'),
    path('view-post/<int:post_id>/', views.view_post, name='view post'),
    path('edit-post/<int:post_id>/', views.edit_post, name='edit post'),
    path('delete/<int:id>/', views.delete_post, name='delete post'),
]