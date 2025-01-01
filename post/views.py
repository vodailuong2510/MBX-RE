from django.shortcuts import render
from .forms import PostForm, SellerForm
from django.shortcuts import redirect

# Create your views here.def create_post(request):
def create_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        sellerForm = SellerForm(request.POST)

        if postForm.is_valid() and sellerForm.is_valid():
            post = postForm.save()
            seller = sellerForm.save()

            post.author = request.user
            post.save()
            seller.post = post
            seller.save()

            return redirect('home') 
    else:
        postForm = PostForm()
        sellerForm = SellerForm()

    return render(request, 'create_post.html', {'postForm': postForm, 'sellerForm': sellerForm})