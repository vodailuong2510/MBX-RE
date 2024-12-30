from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import MyAuthForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=MyAuthForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot password'),
    path('change-password/', views.change_password, name='change password'),
]