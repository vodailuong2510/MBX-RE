from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
from .models import Post

import logging

logger = logging.getLogger(__name__)

# Create your views here.def create_post(request):
def create_post(request):
    if request.method == 'POST':
        print(request.POST)
        postForm = PostForm(request.POST, request.FILES)

        if postForm.is_valid():
            post = postForm.save()

            post.author = request.user
            post.save()
            return redirect('home') 
    else:
        postForm = PostForm()

    return render(request, 'create_post.html', {'postForm': postForm})

def view_posts(request):
    # Get all posts
    all_posts = Post.objects.all()
    
    # Get posts ordered by creation date (newest first)
    posts_by_date = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts_by_date})
    