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
            messages.success(request, 'Successfully registered')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'register.html', {'form' : form})

# def forgot_password(request):
#     form = ForgotPasswordForm()
#     if request.method == 'POST':
#         form = ForgotPasswordForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Mật khẩu mới đã được gửi tới email của bạn.')
#             return HttpResponseRedirect(reverse('login'))
#     return render(request, 'forgot_password.html', {'form' : form})

# def change_password(request):
#     form = ChangePasswordForm()
#     if request.method == 'POST':
#         form = ChangePasswordForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Mật khẩu của bạn đã được thay đổi.')
#             return HttpResponseRedirect(reverse('login'))
#     return render(request, 'change_password.html', {'form' : form})

def profile(request):
    return render(request, 'profile.html')

def postManagement(request):
    return render(request, 'post_management.html')