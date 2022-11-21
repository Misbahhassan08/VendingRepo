
from time import sleep
import paho.mqtt.client as paho

class Main:
    broker="broker.emqx.io"
    i = 0
    def on_message(client, userdata, message):
        sleep(1)
        print(f"topic = {message.topic} and received message = {message.payload} ")
    client= paho.Client() #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
    ######Bind function to callback
    client.on_message=on_message
    #####
    print("connecting to broker ",broker)
    while True:
        i += 1
        client.connect(broker, 1883, 8083)#connect
        client.loop_start() #start loop to process received messages
        print("subscribing ")
        client.subscribe("rpi1/ping")#subscribe
        sleep(2)
        print("publishing ")
        client.publish("rpi1/ping", i)#publish
        sleep(4)
        #client.disconnect() #disconnect
        client.loop_stop() #stop loop

    pass   # end of main class




