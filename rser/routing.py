# routing.py 定义websocket路由
from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/mqtt/', consumers.MyConsumer),
]