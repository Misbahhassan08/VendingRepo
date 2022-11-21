from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import threading
from PyQt5.QtCore import QThread,pyqtSignal
class Reader(QThread):
    signalFlow = pyqtSignal(str,str,name='m_signal')
    def __init__(self):
        QThread.__init__(self)
        self.reader = SimpleMFRC522()
        self.start()
        pass    # end of init
    def run(self):
        while True:
            id, text = self.reader.read()
            sleep(0.5)
            if id == 419700483814 :
                #return ["Teacher_1", id, "Present"]
                print(id)
                self.signalFlow.emit(str(id),'RFID')
                #return id
            elif id == 417650910869 :
                #return ["Teacher_2", id, "Present"]
                self.signalFlow.emit(str(id),'RFID')
                #return id
            elif id == 1076670962393 :
                #return ["Student_1", id, "Present"]
                self.signalFlow.emit(str(id),'RFID')
                #return id
            elif id == 412488440394 :
                #return ["Student_2", id, "Present"]
                self.signalFlow.emit(str(id),'RFID')
                #return id
            elif id == 757966053799 :
                #return ["Student_3", id, "Present"]
                self.signalFlow.emit(str(id),'RFID')
                #return id
            elif id == 520356793468 :
                #return ["Student_4", id, "Present"]
                self.signalFlow.emit(str(id),'RFID')
                #return id
            elif id == 347386419827 :
                #return ["Student_5", id, "Present"]
                self.signalFlow.emit(str(id),'RFID')
                #return id
        pass    # end of rfid_read
    
if __name__ == "__main__":
    read = Reader()
    #while True:
       #data = read.get_data()
       #print(data)
