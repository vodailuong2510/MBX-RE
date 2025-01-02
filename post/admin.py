from django.contrib import admin
from .models import Post
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'product', 'price', 'province', 'created_at')
    list_filter = ('product', 'province', 'created_at')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)
    actions = ['delete_selected']

    # Optional: Add confirmation message after deletion
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, f"{queryset.count()} posts were successfully deleted.")

    # Optional: Add confirmation message after single deletion
    def delete_model(self, request, obj):
        obj.delete()
        self.message_user(request, f"The post '{obj.title}' was successfully deleted.")
        
    def delete_button(self, obj):
        return format_html(
            '<a class="deletelink" href="{}/delete/">Delete</a>',
            obj.id
        )
    delete_button.short_description = 'Delete'
    delete_button.allow_tags = True