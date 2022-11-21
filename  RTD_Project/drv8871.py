import pigpio 



class DRV8871:
    def __init__(self):
        self.pi1 = pigpio.pi()
        pass # end of __init__
    def hard_pwm_in1(self,frequency,dutycycle):
        self.pin = 12
        self.pi1.hardware_PWM(self.pin,frequency,dutycycle*10000) # 800Hz 25% dutycycle
    def hard_pwm_in2(self,Frequency,Dutycycle):
        self.pin = 13
        self.pi1.hardware_PWM(self.pin,Frequency,Dutycycle*10000) # 800Hz 25% dutycycle
    pass    # end of drv8871