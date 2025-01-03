from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.def create_post(request):
@login_required
def create_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES)

        if postForm.is_valid():
            post = postForm.save()

            post.user = request.user
            post.save()
            return redirect('home') 
    else:
        postForm = PostForm()

    return render(request, 'create_post.html', {'postForm': postForm})

def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'view_post.html', {'post': post})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES, instance=post)

        if postForm.is_valid():
            post = postForm.save()
            post.save()
            return redirect('home')
    else:
        postForm = PostForm(instance=post)

    return render(request, 'edit_post.html', {'postForm': postForm})