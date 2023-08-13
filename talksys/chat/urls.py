from django.urls import path 
from .views import create_room, admin, room

app_name = 'chat'

urlpatterns = [
    path('api/create-room/<str:uuid>/',create_room,name='create-room'),
    path('chat-admin/', admin, name='admin'),
    path('chat-admin/<str:uuid>/',room, name='room'),
]
