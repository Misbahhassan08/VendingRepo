import pigpio 

class MAX31865:
    def __init__(self):
        self.pi1 = pigpio.pi()
        self.pi1.spi_open(0,50000,3)
        pass                                                     # end of__init__
    def read_data(self):
        (self.b,self.d) = self.pi1.spi_read(0,60)                     # read 60 bytes from device h
        if self.b == 60:
            return self.d
        else:
            print("Get_data Function Error")
        pass                                                     # end of read data
    def write_data(self,write_data):
        self.pi1.spi_write(0,write_data)                     # write data
        pass                                                     # end of write data
    pass                                                         #end of max31865

if __name__ == "__main__":
    max31865 = MAX31865()