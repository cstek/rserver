# routing.py

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from rser import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/time/", consumers.TimeConsumer),
    ]),
})
