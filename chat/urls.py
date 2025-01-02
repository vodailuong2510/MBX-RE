from django.urls import path
from . import views

urlpatterns = [
    path('get_messages/<str:username>/', views.get_messages, name='get_messages'),
]
