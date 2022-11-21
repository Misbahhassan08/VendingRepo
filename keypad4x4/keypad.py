

# these GPIO pins are connected to the keypad
# change these according to your connections!
class keypad_4x4:

    pass   # end of main class
    def __init__(self,pi1,R1,R2,R3,R4):
        # Initialize the GPIO pins
        self.pi1 = pi1
        self.R1 = R1
        self.R2 = R2
        self.R3 = R3
        self.R4 = R4
        
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
        
        pass   # end of init
    
# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column  
    
    def readLine(self,line,characters):
        self.pi1.write(line,1)
        if(self.pi1.read(self.C1) == 1):
            print(characters[0])
        if(self.pi1.read(self.C2) == 1):
            print(characters[1])
        if(self.pi1.read(self.C3) == 1):
            print(characters[2])
        if(self.pi1.read(self.C4) == 1):
            print(characters[3])
        self.pi1.write(line,0)
        pass   # end of read
    def keypad_value(self):
        pass    # end of keypad
    
if __name__ == "__main__":
    from time import sleep
    import pigpio
    R1 = 6
    R2 = 13
    R3 = 19
    R4 = 26
    pi = pigpio.pi()
    keypad = keypad_4x4(pi,R1,R2,R3,R4)
    try:
        while True:
            # call the readLine function for each row of the keypad
            keypad.readLine(R1, ["1","2","3","A"])
            keypad.readLine(R2, ["4","5","6","B"])
            keypad.readLine(R3, ["7","8","9","C"])
            keypad.readLine(R4, ["*","0","#","D"])
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nApplication stopped!")
    








