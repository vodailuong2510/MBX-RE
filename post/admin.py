from django.contrib import admin
from .models import Post
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

class ClubAdmin(admin.ModelAdmin):
    list_display = ['image', 'product', 'title', 'price', 'description', 'province', 'district', 'ward']
    
    
    
admin.site.register(Post, ClubAdmin)