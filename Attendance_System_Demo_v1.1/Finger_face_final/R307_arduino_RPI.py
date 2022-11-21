from time import sleep
import pigpio
from PyQt5.QtCore import QThread,pyqtSignal
class R307(QThread):
    pi1 = pigpio.pi()
    signalFlow = pyqtSignal(str,str,name='m_signal')
    def __init__(self):
        QThread.__init__(self)
        self.h = self.pi1.i2c_open(0x01,0x08)
        self.start()
        pass    # end of __init__
    def run(self):
        while True:
            self.count,self.data = self.pi1.i2c_read_i2c_block_data(self.h,0x08,1)
            if self.count > 0:
                if self.data[0] >=1 :
                    #print("sdfsd")
                    self.signalFlow.emit(str(self.data[0]),'finger')
        pass
    def write(self,string):
        self.pi1.i2c_write_i2c_block_data(self.h,0x08,string)
        sleep(0.5)
        #self.pi1.i2c_close(self.h)
        pass     # end of write

if __name__ == "__main__":
    from time import sleep
    import pigpio
    pi = pigpio.pi()
    r307 = R307()
    sleep(0.5)
    
    while True:
        
        print("While is running")
        #r307.write('1')
        
        #data = r307.get_ID()
        sleep(0.5)
        #print(data)
        #pi.stop()
    
    