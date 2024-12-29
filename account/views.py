from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bạn đã đăng ký tài khoản thành công.')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'register.html', {'form' : form})

def forgot_password(request):
    return render(request, 'forgot_password.html')

def change_password(request):
    return render(request, 'change_password.html')