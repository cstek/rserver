"""
ASGI config for rserver project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rserver.settings')
#
# application = get_asgi_application()

import os

from django.urls import path
from rser.consumers import TimeConsumer
import rserver.routing
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import rser.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rserver.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/time/", TimeConsumer.as_asgi()),
        ])
    ),
})