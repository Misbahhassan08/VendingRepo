import pigpio
import threading
from PyQt5.QtCore import QThread,pyqtSignal
from time import sleep
# these GPIO pins are connected to the keypad
# change these according to your connections!
class keypad_4x4(QThread):
    signalFlow = pyqtSignal(str,str,name='m_signal')
    pi1 = pigpio.pi()
    pass   # end of main class
    def __init__(self):
        QThread.__init__(self)
        # Initialize the GPIO pins
        self.R1 = 6
        self.R2 = 13
        self.R3 = 19
        self.R4 = 26
        
        self.temp = None
        self.Line = [self.R1, self.R2, self.R3, self.R4]
        self.Characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]
        
        self.C1 = 12
        self.C2 = 16
        self.C3 = 20
        self.C4 = 21
        
        self.pi1.set_mode(self.R1,pigpio.OUTPUT)
        self.pi1.set_mode(self.R2,pigpio.OUTPUT)
        self.pi1.set_mode(self.R3,pigpio.OUTPUT)
        self.pi1.set_mode(self.R4,pigpio.OUTPUT)
        
        self.pi1.set_mode(self.C1,pigpio.INPUT)
        self.pi1.set_mode(self.C2,pigpio.INPUT)
        self.pi1.set_mode(self.C3,pigpio.INPUT)
        self.pi1.set_mode(self.C4,pigpio.INPUT)

        # Make sure to configure the input pins to use the internal pull-down resistors

        self.pi1.set_pull_up_down(self.C1,pigpio.PUD_DOWN)
        self.pi1.set_pull_up_down(self.C2,pigpio.PUD_DOWN)
        self.pi1.set_pull_up_down(self.C3,pigpio.PUD_DOWN)
        self.pi1.set_pull_up_down(self.C4,pigpio.PUD_DOWN)
        
        self.start()
        
        pass   # end of init
    
# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column  
    
    def readLine(self,line,characters):
        self.line = line
        self.characters = characters
        self.temp = None
        self.pi1.write(self.line,1)
        if(self.pi1.read(self.C1) == 1):
            self.temp = self.characters[0]
        elif(self.pi1.read(self.C2) == 1):
            self.temp = self.characters[1]
        elif(self.pi1.read(self.C3) == 1):
            self.temp = self.characters[2]
        elif(self.pi1.read(self.C4) == 1):
            self.temp = self.characters[3]
        self.pi1.write(self.line,0)
        sleep(0.05)
        return self.temp
        pass   # end of read
    def run(self):
        while True:
            for i in range (0, 4):
                self.data = self.readLine(self.Line[i], self.Characters[i])
                if self.data is not None:
                    self.signalFlow.emit(str(self.data),'Pascode')
               
        pass   # end of keypad_value
    
#if __name__ == "__main__":
   # from time import sleep
    
   # keypad = keypad_4x4()
    #while True:
        # call the readLine function for each row of the keypad
      # vv = keypad.keypad_value()
       #print(vv) 
    








