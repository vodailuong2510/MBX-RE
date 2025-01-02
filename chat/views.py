from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
# Create your views here.


@require_GET
def get_messages(request, username):
    receiver = User.objects.get(username=username)
    messages = Message.objects.filter(
        (models.Q(sender=request.user, receiver=receiver) |
         models.Q(sender=receiver, receiver=request.user))
    ).order_by('timestamp')
    
    message_list = []
    for message in messages:
        message_list.append({
            'sender': message.sender.username,
            'content': message.content,  
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        })
    
    return JsonResponse({'messages': message_list})