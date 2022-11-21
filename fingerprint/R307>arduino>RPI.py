from time import sleep
class R307:
    def __init__(self,pi1):
        self.pi1 = pi1
        self.h = self.pi1.i2c_open(0x01,0x08)
        pass    # end of __init__
    def read(self):
        self.count,self.data = self.pi1.i2c_read_i2c_block_data(self.h,0x08,1)
        if self.count > 0:
            if self.data == 255 :
                self.data =0
            print(f"count : {self.count}")
            return self.data[0]
            
        sleep(0.5)
        #self.pi1.i2c_close(self.h)
        pass    # end of read
    def write(self,string):
        self.pi1.i2c_write_i2c_block_data(self.h,0x08,string)
        sleep(0.5)
        #self.pi1.i2c_close(self.h)
        pass     # end of write

if __name__ == "__main__":
    from time import sleep
    import pigpio
    pi = pigpio.pi()
    r307 = R307(pi)
    sleep(0.5)
    
    while True:
        
        print("While is running")
        #r307.write('1')
        
        data = r307.read()
        sleep(0.5)
        print(data)
        #pi.stop()
    
    