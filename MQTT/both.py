from time import sleep
import paho.mqtt.client as mqtt

class Main:
    
    
    broker = "broker.emqx.io"
    def __init__(self):
        self.i = "Muhammad Atif Rafique"
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.will_set('raspberry/status', b'{"status": "Off"}')
        self.client.connect("broker.emqx.io", 1883, 8083)
        self.client.subscribe("raspberry/topic")
        sleep(2)
        self.client.publish('raspberry/topic', payload=self.i, qos=0, retain=False)
        sleep(4)
        self.client.loop_forever()
        pass   # end init function
    def on_message(client, userdata, msg):
            print(f"{msg.topic} {msg.payload}")
            pass   # end of on_message
    def on_connect(client, userdata, flags, rc):
            print(f"Connected with result code {rc}")
    
    pass   # end of Main Class

if __name__ == "__main__":
    main = Main()