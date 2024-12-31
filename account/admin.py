from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Register your models here.
def ban_user(BaseUserAdmin, request, queryset):
    queryset.update(is_active=False)

def unban_user(BaseUserAdmin, request, queryset):
    queryset.update(is_active=True) 

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined') 
    actions = [ban_user, unban_user]  

# Đăng ký lại UserAdmin với các hành động mới
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)