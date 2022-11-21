from time import sleep
import sys
from mfrc522 import SimpleMFRC522

class Reader:
    def __init__(self):
        self.reader = SimpleMFRC522()
        pass    # end of init
    def get_data(self):
        print("Hold a tag near the reader")
        id, text = self.reader.read()
        sleep(0.5)
        if id == 419700483814 :
            return ["Teacher_1", id, "Present"]
        elif id == 417650910869 :
            return ["Teacher_2", id, "Present"]
        elif id == 1076670962393 :
            return ["Student_1", id, "Present"]
        elif id == 412488440394 :
            return ["Student_2", id, "Present"]
        elif id == 757966053799 :
            return ["Student_3", id, "Present"]
        elif id == 520356793468 :
            return ["Student_4", id, "Present"]
        elif id == 347386419827 :
            return ["Student_5", id, "Present"]
        pass    # end of rfid_read
    
if __name__ == "__main__":
    read = Reader()
    while True:
       data = read.get_data()
       print(data)
