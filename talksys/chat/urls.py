from django.urls import path 
from .views import create_room, admin, room, add_user,user_detail,edit_user,delete_room

app_name = 'chat'

urlpatterns = [
    path('api/create-room/<str:uuid>/',create_room,name='create-room'),
    path('chat-admin/', admin, name='admin'),
    path('chat-admin/add-user/',add_user, name='add_user'),
    path('chat-admin/users/<uuid:uuid>/', user_detail, name='user_detail'), 
    path('chat-admin/users/<uuid:uuid>/edit/', edit_user, name='edit_user'), 
    path('chat-admin/<str:uuid>/',room, name='room'),
    path('chat-admin/<str:uuid>/delete/',delete_room, name='delete_room'),
]
