from django.db import models
from .models import Message
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
import json
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

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sender = request.user
            receiver_username = data['receiver']
            content = data['content']

            receiver = User.objects.get(username=receiver_username)

            Message.objects.create(sender=sender, receiver=receiver, content=content)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})