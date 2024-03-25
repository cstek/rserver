# consumer.py 处理 WebSocket 连接、接收消息和发送消息
# consumers.py

import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
import json


class TimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            # 发送当前时间到 WebSocket
            await self.send(json.dumps({'time': str(datetime.datetime.now())}))
            await asyncio.sleep(1)  # 每秒发送一次

    async def disconnect(self, close_code):
        pass
