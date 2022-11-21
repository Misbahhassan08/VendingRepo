from keypad import keypad_4x4
from time import sleep

class Main:
    def __init__(self):
        self.Passcode = keypad_4x4()
        self.Passcode.signalFlow.connect(self.passcode)
        self.code = -1
        self.name = ""
        pass   # end of __ini__ function
    def passcode(self,Code,Name):
        self.code = Code
        self.name = name
        self.print(self.name)
        pass  # end of passcode function
    def whle(self):
        while True:
            sleep(1)
            print(f"passcode = {self.code} and Name = {self.name}")
        pass   # en of whle function
    pass  # End of Main classs

if __name__ == "__main__":
    main = Main()
    main.whle()