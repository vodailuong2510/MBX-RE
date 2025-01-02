from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'product', 'title', 'price', 'description', 'province', 'district', 'ward']

    product_choices = [
        ('', '---Select Product---'),
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('truck', 'Truck'),
    ]
    
    product = forms.ChoiceField(label='Category', choices=product_choices, widget=forms.Select(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Post category'
        })
    )
    
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Title'
        })
    )
    
    price = forms.IntegerField(label='Price', widget=forms.NumberInput(attrs={
            'type': 'number',
            'class': 'post-form',
            'placeholder': 'Price'
        })
    )
    
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Description',
            'maxlength': '300',
            'style': 'resize: vertical; max-height: 150px;',
        })
    )
    
    PROVINCE_CHOICES = [
        ('', '---Select Province/City---'),
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
            'placeholder': 'Province/City'
        })
    )
    
    district = forms.ChoiceField(label='District', choices=DISTRICT_CHOICES, widget=forms.Select(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'District'
        })
    )
    
    ward = forms.ChoiceField(label='Ward', choices=WARD_CHOICES, widget=forms.Select(attrs={
            'type': 'text',
            'class': 'post-form',
            'placeholder': 'Ward'
        })
    )
    
    def clean(self):
        price = self.cleaned_data['price']
        description = self.cleaned_data['description']

        if not isinstance(price, (int, float)) or price < 0:
            raise forms.ValidationError('The price must be a number and cannot be less than 0')
        
        if len(description) < 50:
            raise forms.ValidationError('The description must contain at least 50 characters')
        
        return self.cleaned_data