import pigpio 


class DRV8834_4:
    def __init__(self):
        self.pi1 = pigpio.pi()
        self.step_pin = 26
        self.dir_pin = 20
        self.high = 1
        self.low = 0
        self.pi1.set_mode(self.dir_pin, pigpio.OUTPUT)
        self.pi1.set_mode(self.step_pin, pigpio.OUTPUT)
        pass   # end of __init__
    def step_high(self):
        self.pi1.write(self.step_pin,self.high)
        pass   # end of step high
    def step_low(self):
        self.pi1.write(self.step_pin,self.low)
        pass   # end of step low
    def dir_high(self):
        self.pi1.write(self.dir_pin,self.high)
        pass   #end of dir high
    def dir_low(self):
        self.pi1.write(self.dir_pin,self.low)
        pass   #end of dir low
    pass    #end of drv8834_4