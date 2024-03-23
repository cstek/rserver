# mqtt_client.py
# import paho.mqtt.client as mqtt
#
# # MQTT服务器设置
# MQTT_HOST = 'localhost'
# MQTT_PORT = 1883
# MQTT_TOPIC = 'fromEsp'
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
for i in range(10):
    print(i)