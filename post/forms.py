from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from django.contrib.auth.forms import AuthenticationForm

class PostForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', '---Select Category---'),
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('truck', 'Truck'),
    ]
    
    category = forms.ChoiceField(label='Category', choices=CATEGORY_CHOICES, widget=forms.Select(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Post category'
        })
    )
    
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Title *'
        })
    )
    
    brand = forms.CharField(label='Brand', widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Brand *'
        })
    )
    
    status = forms.CharField(label='Status', widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Status *'
        })
    )
    
    price = forms.IntegerField(label='Price', widget=forms.NumberInput(attrs={
            'type': 'number',
            'class': 'post-form',
            'placeholder': 'Price *'
        })
    )
    
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Description *',
            'maxlength': '300',
            'style': 'resize: vertical; max-height: 150px;',
        })
    )
    
class SellerForm(forms.Form):
    PROVINCE_CHOICES = [
        ('', '---Select Province---'),
        ('hanoi', 'Hanoi'),
        ('hochiminh', 'Ho Chi Minh City'),
        ('danang', 'Da Nang'),
    ]
    
    DISTRICT_CHOICES = [
        ('', '---Select District---'),
        ('district1', 'District 1'),
        ('district2', 'District 2'),
        ('district3', 'District 3'),
    ]
    
    WARD_CHOICES = [
        ('', '---Select Ward---'),
        ('ward1', 'Ward 1'),
        ('ward2', 'Ward 2'),
        ('ward3', 'Ward 3'),
    ]
    
    province = forms.ChoiceField(label='Province', choices=PROVINCE_CHOICES, widget=forms.Select(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Province/City *'
        })
    )
    
    district = forms.ChoiceField(label='District', choices=DISTRICT_CHOICES, widget=forms.Select(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'District *'
        })
    )
    
    ward = forms.ChoiceField(label='Ward', choices=WARD_CHOICES, widget=forms.Select(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Ward *'
        })
    )
    
    detailedAddress = forms.CharField(label='Detailed Address', widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Detailed address *'
        })
    )