# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TCS34725
# This code is designed to work with the TCS34725_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

import smbus
import time
class TCS34725:
    # Get I2C bus
    Bus = smbus.SMBus(1)
    Bus.write_byte_data(0x70,0, 0x02)   # select mux channel 2
    def __init__(self):
        #uncomment self.setup when First time run programme after shuton raspberry pi
        #self.setup()
        pass   # end of init
    def setup(self):
        # TCS34725 address, 0x29(41)
        # Select Enable register, 0x80(128)
        #		0x03(03)	Power ON, RGBC enable, RGBC Interrupt Mask not asserted
        #					Wait disable, Sleep After Interrupt not asserted
        self.Bus.write_byte_data(0x29, 0x80, 0x03)
        # TCS34725 address, 0x29(41)
        # Select RGBC Timing register, 0x81(129)
        #		0x00(00)	ATIME : 700ms
        self.Bus.write_byte_data(0x29, 0x81, 0x00)
        # TCS34725 address, 0x29(41)
        # Select Wait Time register, 0x83(131)
        #		0xFF(255)	WTIME : 2.4ms
        self.Bus.write_byte_data(0x29, 0x83, 0xFF)
        # TCS34725 address 0x29(41)
        # Select Control register, 0x8F(143)
        #		0x00(00)	AGAIN is 1x
        self.Bus.write_byte_data(0x29, 0x8F, 0x00)
        pass   # end of setup
    def read_and_convert(self):
        # TCS34725 address 0x29(41)
        # Read data back from 0x94(148), 8 bytes
        # cData LSB, cData MSB, Red LSB, Red MSB, Green LSB, Green MSB
        # Blue LSB, Blue MSB 
        data = self.Bus.read_i2c_block_data(0x29, 0x94, 8)

        # Convert the data
        cData = data[1] * 256 + data[0]
        red = data[3] * 256 + data[2]
        green = data[5] * 256 + data[4]
        blue = data[7] * 256 + data[6]

        # Calculate luminance
        luminance = (-0.32466 * red) + (1.57837 * green) + (-0.73191 * blue)

        # Output data to screen
        print("Red Color luminance : %d lux" %red)
        print("Green Color luminance : %d lux" %green)
        print("Blue Color luminance : %d lux" %blue)
        print("IR luminance : %d lux" %cData)
        print("Ambient Light luminance : %.2f lux" %luminance)
        
if __name__ == "__main__":
    mux = TCS34725()
    while True:
        mux.read_and_convert()
        
        
        dfgdg
