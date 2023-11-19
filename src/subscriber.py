import paho.mqtt.client as paho

class Subscriber:

    BROKER_HOST = "127.0.0.1"
    BROKER_PORT = 1883

    def __init__(self, topic):
        self.topic = topic
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload.decode()}")

    def start(self):
        self.client.connect(self.BROKER_HOST, self.BROKER_PORT, 60)
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()


