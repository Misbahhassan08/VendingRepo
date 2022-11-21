from publisher import Publisher
from time import sleep
from subscriber import Subscriber

class Main:
    data = "Muhammad"
    #broker = "broker.emqx.io"
    def __init__(self):
        self.Sub = Subscriber()
        self.Pub = Publisher()
        
        pass   # end on ini Function
    def initialize(self):
        self.Sub.client.connect("broker.emqx.io", 1883, 8083)
        self.Pub.client.connect("broker.emqx.io", 1883, 8083)
        
        pass   # end of initialize
    def Publsh(self):
        while True:
            self.Pub.client.publish('raspberry/topic', payload=data, qos=0, retain=False)
            sleep(1)
            self.Pub.client.loop_forever()
        pass   # end of Publsh
    def Subsc(self):
        self.Sub.client.will_set('raspberry/status', b'{"status": "Off"}')
        self.Sub.client.connect("broker.emqx.io", 1883, 8083)
        self.Sub.client.loop_forever()
        pass   # end of Subsc
    pass   # end of Main Class
if __name__ == "__main__":
    main = Main()
    main.Subsc()
    main.Publsh()