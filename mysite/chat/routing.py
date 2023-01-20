from django.urls import re_path 
from . import consumers

# use re_path as path is too limited
websocket_urlpatterns = [
    # set the route to the chat consumer. the url is which is set in lobby.html with 'let url = `ws://${window.location.host}/ws/socket-server/`'
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]