from django.urls import re_path
from chat_manage import consumers
websocket_urlpatterns = [
    re_path('room/<str:group>/',consumers.ChatConsumer.as_asgi()),
]
