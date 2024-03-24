# consumer.py 处理 WebSocket 连接、接收消息和发送消息
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from datetime import datetime
import json
from asgiref.sync import async_to_sync
import paho.mqtt.client as mqtt


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 连接到MQTT代理服务器
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect("localhost", 1883, 60)
        self.mqtt_client.loop_start()

        # 订阅MQTT主题
        self.mqtt_client.subscribe("fromEsp")

        await self.accept()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT broker with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        # 处理MQTT消息
        message = msg.payload.decode()
        self.send_message(message)

    async def receive(self, text_data):
        # 在接收到前端发送的消息时，将其发布到MQTT主题
        self.mqtt_client.publish("mqtt_topic", text_data)

    async def disconnect(self, code):
        # 断开MQTT连接
        self.mqtt_client.disconnect()
        self.mqtt_client.loop_stop()

    def send_message(self, message):
        # 发送消息到前端页面
        self.send(text_data=message)
    # mqtt_client = None  # 定义MQTT客户端为类变量
    #
    # async def connect(self):
    #     await self.accept()
    #
    #     # 使用async_to_sync包装器调用同步方法
    #     if not MyConsumer.mqtt_client:
    #         async_to_sync(self.setup_mqtt_client)()
    #
    # def setup_mqtt_client(self):
    #     def on_message(client, userdata, message):
    #         # 当MQTT接收到消息时，将其发送到WebSocket
    #         try:
    #             # 注意，这里使用了async_to_sync包装器
    #             async_to_sync(self.send)(text_data=json.dumps({'message': message.payload.decode()}))
    #         except Exception as e:
    #             print(f"Error sending message: {e}")
    #
    #     MyConsumer.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    #     MyConsumer.mqtt_client.on_message = on_message
    #     MyConsumer.mqtt_client.connect("localhost", 1883, 60)
    #     MyConsumer.mqtt_client.subscribe("fromEsp")
    #     MyConsumer.mqtt_client.loop_forever()  # 使用loop_start而不是loop_forever
    #
    # async def disconnect(self, close_code):
    #     if MyConsumer.mqtt_client:
    #         MyConsumer.mqtt_client.loop_stop()  # 停止MQTT客户端循环
    #         MyConsumer.mqtt_client.disconnect()  # 断开MQTT客户端连接
    #         MyConsumer.mqtt_client = None


class TimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 发送 JSON 格式的消息
            await self.send(json.dumps({'time': now}))
            await asyncio.sleep(1)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        pass
