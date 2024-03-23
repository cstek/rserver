# consumer.py 处理 WebSocket 连接、接收消息和发送消息
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
import paho.mqtt.client as mqtt


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # 在新线程中启动MQTT客户端
        asyncio.get_event_loop().run_in_executor(None, self.mqtt_client)

    def mqtt_client(self):
        def on_message(client, userdata, message):
            # 当MQTT接收到消息时，将其发送到WebSocket
            # 注意这里我们需要捕捉异常，因为这个回调是在另一个线程中执行的
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                loop.run_until_complete(self.send(text_data=json.dumps({'message': message.payload.decode()})))
            except Exception as e:
                print(f"Error sending message: {e}")

        client = mqtt.Client()
        client.on_message = on_message
        client.connect("localhost", 1883, 60)

        # 订阅你想要监听的主题
        client.subscribe("fromEsp")

        client.loop_forever()

    async def disconnect(self, close_code):
        # 断开连接时的操作
        pass
