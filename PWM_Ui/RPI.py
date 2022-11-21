import pigpio 
import serial
import threading
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep

class RPI_Class(QThread):
    signalFlow = pyqtSignal(str,str,name='m_signals')
    def __init__(self):
        
        QThread.__init__(self)
        self.pi1 = pigpio.pi()
        self.led = 17
        self.pi1.set_mode(self.led, pigpio.OUTPUT)
        self.led_oon  = 1
        self.led_ooff = 0
        self.d = None
        self.ser = serial.Serial("/dev/ttyUSB0", 9600)
        #self.deamon = True
        self.start()
        
    def led_on(self):
        self.pi1.write(self.led,self.led_oon) 
        
        
    def led_off(self):
        self.pi1.write(self.led,self.led_ooff)
        
        
    def hard_pwm(self,pin,frequency,dutycycle):
        self.pin = pin
        self.frequency = frequency
        self.dutycycle = dutycycle
        self.pi1.hardware_PWM(self.pin, self.frequency, self.dutycycle*10000) # 800Hz 25% dutycycle
    
    def run(self):
        while True:
            self.d = self.ser.readline()
            if self.d is not None:
                self.signalFlow.emit(str(self.d),'Arduino')
                sleep(0.01)
            pass # end of run function 



'''if __name__ == "__main__":
        rpi = RPI_Class()
        #rpi.hard_pwm(18,800,50)'''


