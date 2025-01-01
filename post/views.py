from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.def create_post(request):
def create_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            post = postForm.save()

            post.author = request.user
            post.save()

            return redirect('home') 
    else:
        postForm = PostForm()

    return render(request, 'create_post.html', {'postForm': postForm})