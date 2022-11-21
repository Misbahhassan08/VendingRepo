from time import sleep
import sys
from mfrc522 import SimpleMFRC522
from PyQt5.QtCore import QThread
class Reader(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.reader = SimpleMFRC522()
        self.swap_id = -1
        self.id = -1
        self.start()
        pass    # end of init
    def get_id(self):
        self.swap_id = self.id
        self.id = 0
        return self.swap_id
        pass   # end of get_id function
    def run(self):
        while True:
            self.id, text = self.reader.read()
            print(f"Reader is Working With ID = {self.id}")
            sleep(0.5)
        pass    # end of rfid_read
    
if __name__ == "__main__":
    from time import sleep
    read = Reader()
    while True:
        sleep(1)
        ids = read.get_id()
        print(f"Main {ids}")
    #while True:
       #data = read.get_data()
       #print(data)
