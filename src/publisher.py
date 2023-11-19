import time
import paho.mqtt.client as paho


class Publisher:
    MQTT_BROKER = "127.0.0.1"
    MQTT_PORT = 1883

    def __init__(self, topic):
        self.MQTT_TOPIC = topic
        print(f"Publiser: topic = {self.MQTT_TOPIC}")
        self.listening_client = paho.Client()
        self.listening_client.connect(self.MQTT_BROKER, self.MQTT_PORT)

    def publish_msg(self, msg):
        self.listening_client.publish(self.MQTT_TOPIC, msg)
