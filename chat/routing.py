from django.urls import re_path
from .consumers import GroupChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/group/(?P<group_slug>[^/]+)/$', GroupChatConsumer.as_asgi()),
]