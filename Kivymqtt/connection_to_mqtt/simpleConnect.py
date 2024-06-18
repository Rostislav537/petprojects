from paho.mqtt import client as mqtt_client
import random
import time
import asyncio

class MqttMethods:
    def __init__(self):
        #Данные об mqtt сервере
        self.broker = 'm23.cloudmqtt.com'
        self.port = 13554
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.username = 'uruuzcjw'
        self.password = 'MdwIFlORpIKW'
        self.client = self.connectToServer()

        self.subtopicsData={}

    def connectToServer(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def publishMessage(self, topic, msg):
        result = self.client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def subscribe(self, topic):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            self.subtopicsData[msg.topic].append(msg.payload.decode())

        self.client.subscribe(topic)
        self.client.on_message = on_message
        self.subtopicsData[topic]=[]

    def startConnection(self):
        client = connect_mqtt()
        subscribe(client)
        client.loop_forever()
    def getMessages(self, topic):
        print(self.subtopicsData)
        if topic in self.subtopicsData:
            return self.subtopicsData[topic]
        else:
            return


# python3.6

import random

from paho.mqtt import client as mqtt_client


broker = 'm23.cloudmqtt.com'
port = 13554
topic = "esp07/temp"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = 'uruuzcjw'
password = 'MdwIFlORpIKW'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()