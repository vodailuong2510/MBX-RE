from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import PostForm, SellerForm

# Create your views here.
def create_post(request):
    postForm = PostForm()
    sellerForm = SellerForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mật khẩu của bạn đã được thay đổi.')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'create_post.html', {'postForm' : postForm, 'sellerForm' : sellerForm})