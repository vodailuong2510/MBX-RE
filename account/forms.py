from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    rePassword = forms.CharField(label='Re Password', widget=forms.PasswordInput(attrs={'placeholder': 'Re Password'}))
    phoneNumber = forms.CharField(label='Phone Number', max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        rePassword = self.cleaned_data.get('rePassword')
        
        if password and len(rePassword) < 8:
            raise forms.ValidationError('Invalid password')
        
        if password and rePassword and password != rePassword:
            raise forms.ValidationError('Your passwords do not match')
        
        return rePassword
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 8:
            raise forms.ValidationError('The username must contain at least 8 characters')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username has already existed')

    def clean_phoneNumber(self):
        
        phoneNumber = self.cleaned_data['phoneNumber']
        if not phoneNumber.isdigit() or phoneNumber[0] != '0' or len(phoneNumber) != 10:
            raise forms.ValidationError('Invalid phone number')
        try:
            User.objects.get(first_name=phoneNumber)
        except ObjectDoesNotExist:
            return phoneNumber
        raise forms.ValidationError('The phone number has been used')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com') and not email.endswith('@yahoo.com') and not email.endswith('@hotmail.com'):
            raise forms.ValidationError('Invalid email')
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email has been used')
    
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['phoneNumber'],
            email=self.cleaned_data['email']
        )
        return user