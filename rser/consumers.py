# consumer.py 处理 WebSocket 连接、接收消息和发送消息
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync
import paho.mqtt.client as mqtt


class MyConsumer(AsyncWebsocketConsumer):
    mqtt_client = None  # 定义MQTT客户端为类变量

    async def connect(self):
        await self.accept()

        # 使用async_to_sync包装器调用同步方法
        if not MyConsumer.mqtt_client:
            async_to_sync(self.setup_mqtt_client)()

    def setup_mqtt_client(self):
        def on_message(client, userdata, message):
            # 当MQTT接收到消息时，将其发送到WebSocket
            try:
                # 注意，这里使用了async_to_sync包装器
                async_to_sync(self.send)(text_data=json.dumps({'message': message.payload.decode()}))
            except Exception as e:
                print(f"Error sending message: {e}")

        MyConsumer.mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        MyConsumer.mqtt_client.on_message = on_message
        MyConsumer.mqtt_client.connect("localhost", 1883, 60)
        MyConsumer.mqtt_client.subscribe("fromEsp")
        MyConsumer.mqtt_client.loop_start()  # 使用loop_start而不是loop_forever

    async def disconnect(self, close_code):
        if MyConsumer.mqtt_client:
            MyConsumer.mqtt_client.loop_stop()  # 停止MQTT客户端循环
            MyConsumer.mqtt_client.disconnect()  # 断开MQTT客户端连接
            MyConsumer.mqtt_client = None
