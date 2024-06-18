import time

from  connection_to_mqtt.simpleConnect import MqttMethods
mqtt=MqttMethods()
mqtt.subscribe("esp07/temp")
mqtt.publishMessage("test/test", "Hello")
while True:
    time.sleep(2)
    print(mqtt.getMessages("esp07/temp"))