from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def chat_partners(request):
    if request.user.is_authenticated:
        chat_partners = User.objects.filter(
            Q(sent_messages__receiver=request.user) |
            Q(received_messages__sender=request.user)
        ).distinct()
    else:
        chat_partners = []

    return {'chat_partners': chat_partners}