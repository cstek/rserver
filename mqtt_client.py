# mqtt_client.py
import paho.mqtt.client as mqtt

# MQTT服务器设置
MQTT_HOST = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'fromEsp'
#
#
# # 当接收到MQTT消息时的回调函数
# def on_message(client, userdata, message):
#     print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")
#
#
# # 创建MQTT客户端实例
# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
#
# # 指定回调函数
# client.on_message = on_message
#
# # 连接到MQTT服务器
# client.connect(MQTT_HOST, MQTT_PORT, 60)
#
# # 订阅主题
# client.subscribe(MQTT_TOPIC)
#
# # 开始监听订阅的主题（在后台线程中）
# client.loop_start()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(MQTT_HOST, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()