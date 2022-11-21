import pigpio 

class PCA9535DB:
    def __init__(self):
        self.pi1 = pigpio.pi()
        self.pi1.i2c_open(1,0x53) # initalize i2c_device_1 at adress 0x53
        pass    # end of __init__
    def write_data_byte(self,write_data):    # send data on i2c_device_1
        self.pi1.i2c_write_byte(1,write_data)
        pass        #end of write data byte
    def read_data_byte(self):
        self.data = self.pi1.i2c_read_byte_data(1,1) # 1 mean i2c device and 1 mean read byte from register 17 
        if self.data != 0 and self.data != None:
            return self.data
        pass                                                        # end of read data byte
    pass    # end of pca9535db