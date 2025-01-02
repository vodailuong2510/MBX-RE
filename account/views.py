from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate
from .forms import RegistrationForm, LoginForm, forgot_passwordForm, ResetPasswordForm, change_passwordForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        form = forgot_passwordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            user = User.objects.get(email=email)

            token = user.pk

            
            reset_url = request.build_absolute_uri(reverse('reset_password', args=[token]))

            subject = 'MBX: Reset Your Password'
            message = render_to_string('reset_password_email.html', {
                'reset_url': reset_url,
                'user': user,
            })
            
            email_message = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            email_message.content_subtype = 'html'
            email_message.send()


            return redirect('login')
    else:
        form = forgot_passwordForm()

    return render(request, 'forgot_password.html', {'form': form})

def reset_password(request, token):
    user = get_user_model().objects.get(pk=token)  

    auth_login(request, user)

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data
            user.set_password(new_password)
            user.save()

            auth_login(request, user)

            return redirect('home')
    else:
        form = ResetPasswordForm()

    return render(request, 'reset_password.html', {'form': form, 'user': user})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = change_passwordForm(request.POST, request=request)
        if form.is_valid():
            new_password = form.cleaned_data
            user = request.user
            user.set_password(new_password)
            user.save()

            auth_login(request, user)

            return redirect('home')
    else:
        form = change_passwordForm()

    return render(request, 'change_password.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def postManagement(request):
    return render(request, 'post_management.html')
