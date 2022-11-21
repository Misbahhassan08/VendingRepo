import pigpio 

class Arduino:
    pi1 = pigpio.pi()
    def __init__(self):
        pass                                                     # end of__init__
    def read_data(self):
        self.h = self.pi1.spi_open(0,50000,3)
        self.b,self.d = self.pi1.spi_read(self.h,60)                     # read 60 bytes from device h
        if self.b == 60:
            print(f"Read Data : {self.h} : {self.d}")
        else:
            print("read_data Function Error")
        self.pi1.spi_close(self.h)
        pass                                                     # end of read data
    def write_data(self,write_data):
        self.pi1.spi_write(0,write_data)                     # write data
        pass                                                     # end of write data
    pass                                                         #end of max31865

if __name__ == "__main__":
    arduino = Arduino()
    while True:
        arduino.read_data()
