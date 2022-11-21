import paho.mqtt.client as mqtt
import time

class Publisher:
    i = 'Muhammad Atif Rafique'
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 8083)

    # send a message to the raspberry/topic every 1 second, 5 times in a row 
    # the four parameters are topic, sending content, QoS and whether retaining the message respectively
    client.publish('raspberry/topic', payload=i, qos=0, retain=False)
    print(f"send {i} to raspberry/topic")
    time.sleep(1)
    client.loop_forever()
    
    
'''
if __name__ == "__main__":
    publisher = Publisher()
    print("__main__")
    publisher()
    '''