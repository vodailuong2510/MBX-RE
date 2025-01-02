from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User
# Create your views here.

@login_required
def chat_view(request, username):
    receiver = User.objects.get(username=username)

    messages = Message.objects.filter(
        (models.Q(sender=request.user, receiver=receiver) |
         models.Q(sender=receiver, receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            return redirect('chat_view', username=username)
    else:
        form = MessageForm()

    return render(request, 'chat.html', {
        'receiver': receiver,
        'messages': messages,
        'form': form,
    })