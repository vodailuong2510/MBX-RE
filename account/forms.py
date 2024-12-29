from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

def nbsp(times):
    return format_html('&nbsp;' * times)

class RegistrationForm(forms.Form):
    username = forms.CharField(
        label=format_html('Tên tài khoản{}', nbsp(8)),
        max_length=10,
        widget=forms.TextInput(attrs={
            'type': 'username',
            'class': 'login-form-input',
            'placeholder': 'Username'
        })
    )
    
    phoneNum = forms.CharField(
        label=format_html('Số điện thoại{}', nbsp(10)),
        max_length=10,
        widget=forms.TextInput(attrs={
            'type': 'phone',
            'class': 'login-form-input',
            'placeholder': 'Phone number'
        })
    )
    
    email = forms.EmailField(
        label=format_html('Email{}', nbsp(20)),
        widget=forms.EmailInput(attrs={
            'type': 'email',
            'class': 'login-form-input',
            'placeholder': 'Email'
        })
    )
    
    password = forms.CharField(
        label=format_html('Mật khẩu{}', nbsp(15)),
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'login-form-input',
            'placeholder': 'Password'
        })
    )
    
    reEnterPassword = forms.CharField(
        label='Nhập lại mật khẩu',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'login-form-input',
            'placeholder': 'Re-enter password'
        })
    )
    
class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'Password'}) 
        self.fields['password'].label = False
        
class forgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label=format_html('Email{}', nbsp(20)),
        widget=forms.EmailInput(attrs={
            'type': 'email',
            'class': 'login-form-input',
            'placeholder': 'Email'
        })
    )
    
    OTP = forms.CharField(
        label=format_html('Mã OTP{}', nbsp(20)),
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'login-form-input',
            'placeholder': 'OTP'
        })
    )

class changePasswordForm(forms.Form):
    password = forms.CharField(
        label=format_html('Mật khẩu mới{}', nbsp(15)),
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'login-form-input',
            'placeholder': 'Password'
        })
    )
    
    reEnterPassword = forms.CharField(
        label='Nhập lại mật khẩu',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'login-form-input',
            'placeholder': 'Re-enter password'
        })
    )