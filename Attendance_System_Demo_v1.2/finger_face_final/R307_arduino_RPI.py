from time import sleep
import pigpio
from PyQt5.QtCore import QThread,pyqtSignal
class R307(QThread):
    pi1 = pigpio.pi()
    
    def __init__(self):
        QThread.__init__(self)
        self.h = self.pi1.i2c_open(0x01,0x08)
        self.fid = 0
        self.start()
        pass    # end of __init__
    def get_finger_id(self):
        swap_id = self.fid # swaping finger id with local varible
        self.fid = 0 # make fid back to default value so that no more conflicts happen
        
        return swap_id 
    def run(self):
        while True:
            self.count,self.data = self.pi1.i2c_read_i2c_block_data(self.h,0x08,1)
            if self.count > 0:
                if self.data[0] >=1 :
                    print(f"Found ID from Sensor  = {self.data[0]}")
                    self.fid = self.data[0]
                   
        pass
    def write(self,string):
        self.pi1.i2c_write_i2c_block_data(self.h,0x08,string)
        sleep(0.5)
        #self.pi1.i2c_close(self.h)
        pass     # end of write

if __name__ == "__main__":
    from time import sleep
    pi = pigpio.pi()
    r307 = R307()
    sleep(0.5)
    
    while True:
        print("While is running")
        sleep(0.5)
    
    
