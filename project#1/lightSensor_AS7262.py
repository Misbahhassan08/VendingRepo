import smbus
import time
from config import *
import struct

class lightSensor_As7262:
    # Get I2C bus
    bus = smbus.SMBus(1)
    bus.write_byte_data(TCA9548A_I2C_address, 0, TCA9548A_I2C_bus_number)  # select mux channel 1
    def __init__(self):
        pass    # end of init
    #Function to read a single register
    def read_reg(self, reg_to_read):
        while True:
            status = self.bus.read_byte_data(AS7262_Default_address , AS7262_DEVICE_STATUS_REG)
            #Continue if the write buffer is ready
            if (status & 0b00000010) == 0:
                break
            #Else keep waiting
            else:
                pass
        #When the write buffer is ready, write the value of the register
        #you want to read from into the DEVICE_WRITE_REG (0x01)
        self.bus.write_byte_data(AS7262_Default_address , AS7262_DEVICE_WRITE_REG, reg_to_read)

        #Check the DEVICE_STATUS_REG (0x00) until it indicates
        #that the read buffer contains data
        while True:
            status = self.bus.read_byte_data(0x49, AS7262_DEVICE_STATUS_REG)
            #Continue if the read buffer is ready
            if (status & 0b00000001) == AS7262_DEVICE_WRITE_REG:
                break
            #Else keep waiting
            else:
                pass
        #When the read buffer is ready, read the value from the
        #DEVICE_READ_REG (0x02)
        value = self.bus.read_byte_data(AS7262_Default_address , 0x02)
        return value

    #Function to write to a single virtual register
    def write_reg(self, reg_to_write_to, command_to_write):
        #Check the DEVICE_STATUS_REG (0x00) until it indicates
        #that the write buffer is ready to be written to
        while True:
            status = self.bus.read_byte_data(AS7262_Default_address , AS7262_DEVICE_STATUS_REG)
            #Continue if the write buffer is ready
            if (status & 0b00000010) == 0:
                break
            #Else keep waiting
            else:
                pass

        self.bus.write_byte_data(AS7262_Default_address , AS7262_DEVICE_WRITE_REG, (reg_to_write_to | 0x80))
        while True:
            status = self.bus.read_byte_data(AS7262_Default_address , AS7262_DEVICE_STATUS_REG)

            if (status & 0b00000010) == 0:
                break
            #Else keep waiting
            else:
                pass
        #When the write buffer is ready, send DEVCE_WRITE_REG (0x01) the
        #command to be written into the register sent previously
        self.bus.write_byte_data(AS7262_Default_address , AS7262_DEVICE_WRITE_REG, command_to_write)

    #Function to take a single measurement and return the ROYGBV values
    def take_single_measurement(self):
        #Put the device into single-shot mode
        self.set_measurement_mode(3)
        #Get and return the values
        readings = self.get_calibrated_values()
        return readings

    #Function to get, process and return the calibrated ROYGBV values
    def get_calibrated_values(self):
        #Wait for data to arrive into the data registers
        #by checking the DATA_RDY bit of the Control Setup reg
        #Return None if waiting for more than 10 seconds
        start = time.time()
        while True:
            state = self.read_reg(0x04)
            #If the data is ready then break to the next stage
            if (state & 0b00000010) == 0b00000010:
                break
            #Otherwise keep waiting, or quit if waited more than 10s
            else:
                if (time.time() >= (start + 10)):
                    print("Error, no data available. Did you use set_measurement_mode() to tell the device to take a reading?")
                    return
                else:
                    pass
        #Read all of the calibrated results into colour_bytes[]
        colour_bytes = []
        for x in range (0x14, 0x2C):
            colour_bytes.append(self.read_reg(x))
        
        #Split the bytes by colour and place into colour specific lists getting IEEE 754 standard floats
        VV = [colour_bytes[0], colour_bytes[1], colour_bytes[2],colour_bytes[3]]
        BB = [colour_bytes[4], colour_bytes[5], colour_bytes[6],colour_bytes[7]]
        GG = [colour_bytes[8], colour_bytes[9], colour_bytes[10],colour_bytes[11]]
        YY = [colour_bytes[12], colour_bytes[13], colour_bytes[14],colour_bytes[15]]
        OO = [colour_bytes[16], colour_bytes[17], colour_bytes[18],colour_bytes[19]]
        RR = [colour_bytes[20], colour_bytes[21], colour_bytes[22],colour_bytes[23]]

        #Convert the values from IEEE 754 standard floats to Python floats,
        #place in calibrated_values list in the order [R,O,Y,G,B,V]
        calibrated_values = []
        calibrated_values.append(struct.unpack('>f', bytearray(RR))[0])
        calibrated_values.append(struct.unpack('>f', bytearray(OO))[0])
        calibrated_values.append(struct.unpack('>f', bytearray(YY))[0])
        calibrated_values.append(struct.unpack('>f', bytearray(GG))[0])
        calibrated_values.append(struct.unpack('>f', bytearray(BB))[0])
        calibrated_values.append(struct.unpack('>f', bytearray(VV))[0])

        return calibrated_values

    def take_single_measurement_with_led(self):
        self.enable_main_led()
        readings = self.take_single_measurement()
        self.disable_main_led()
        return readings

    #Function to return the temperature in degrees C from the sensor
    def get_temperature(self):
        temperature = self.read_reg(0x06)
        return temperature

    #Function to return the temperature in degrees F from the sensor
    def get_temperature_f(self):
        temperature = self.read_reg(0x06) * 1.8 + 32
        return temperature

    #Function to turn on the main illumination LED
    def enable_main_led(self):
        #Read the current state of the LEDs from the device
        current_state = self.read_reg(AS7262_DEVICE_LED)	
        #Set the bit for controlling the main LED to 1 (on) while
        #keeping the other bits as they were
        new_state = current_state | 0b00001000
        #Update the device
        self.write_reg(AS7262_DEVICE_LED , new_state)

    #Function to turn off the main LED
    def disable_main_led(self):
        #Read the current state of the LEDs from the device
        current_state = self.read_reg(AS7262_DEVICE_LED)
        #Set the bit controlling the main LED to 0 (off),
        # keep the other bits as they were
        new_state = current_state & 0b11110111
        #Update the device
        self.write_reg(AS7262_DEVICE_LED, new_state)

    #Function to turn on the indicator LED
    def enable_indicator_led(self):
        #Get the current state of the LEDs
        _current_state = self.read_reg(AS7262_DEVICE_LED)
        #Set the bit controlling the indicator LED to 1 (on),
        new_state = _current_state | 0b00000001
        #Update the device
        self.write_reg(AS7262_DEVICE_LED, new_state)

    #Function to turn off the indicator LED
    def disable_indicator_led(self):
        #Get the current state of the LEDs
        current_state = self.read_reg(AS7262_DEVICE_LED)
        #Set the bit controlling the indicator LED to 0 (off),
        # while keeping the other bits as they were
        new_state = current_state & 0b11111110
        #Update the device
        self.write_reg(AS7262_DEVICE_LED, new_state)

    def set_measurement_mode(self,mode):
        #Check that the reqested mode is valid
        if mode in (0, 1, 2, 3):
            #Get the current settings
            current_state = self.read_reg(0x04)
            #Blank the current mode bits, keep the rest
            current_state = current_state & 0b11110011
            #The mode bits are no. 2&3, so shift the requested mode to match
            mode = mode << 2
            #Add the requested mode to the other current settings
            new_state = current_state | mode
            #Update the device
            self.write_reg(0x04, new_state)
        else:
            print("Error! set_measurement_mode requires a value of 0-3. Value given was " + str(mode) + ".")
        
    #Function to set the current on the indicator LED, takes int value from 0-3
    #0 = 1 mA, 1 = 2 mA, 2 = 4 mA, 3 = 8 mA
    def set_indicator_current(self, current_level):
        #Check that the requested current_level is valid
        if current_level in (0, 1, 2, 3):
            #Get the current state of the LEDs
            current_state = self.read_reg(AS7262_DEVICE_LED)
            #Blank the current for the indicator LED
            new_state = current_state & 0b00111001
            #Indicator current bits are 1&2, so shift current_level to match
            current_level = current_level << 1
            #Insert the requested current_level into the LED control byte
            new_state = new_state | current_level
            #Update the device
            self.write_reg(AS7262_DEVICE_LED, new_state)
        else:
            print("Error! set_indicator_current requires a value of 0-3. Value given was " + str(current_level) + ".")
        
    #Function to set the current on the LED, takes a value from 0-3
    #0 = 12.5 mA, 1 = 25 mA, 2 = 50 mA, 3 = 100 mA
    def set_led_current(self, current_level):
    #Check that the requested current_level is valid
        if current_level in (0, 1, 2, 3):
            #Get the current state of the LEDs
            current_state = self.read_reg(AS7262_DEVICE_LED)
            #Blank the bits controlling the bulb current
            new_state = current_state & 0b00001111
            #Bitshift the requested current_level to match the required position
            current_level = current_level << 4
            #Insert the current_level into the LED control byte
            new_state = new_state | current_level
            #Update the device with the new settings
            self.write_reg(AS7262_DEVICE_LED, new_state)
        else:
            print("Error! set_bulb_current requires a value of 0-3.  Value given was " + str(current_level) + ".")


    #Function to soft reset the chip
    def soft_reset(self):
        #Write the reset value to the register controlling the reset function
        self.write_reg(AS7262_DEVICE_SETUP_REG, 0b10000000)
        #Wait for the device to reset (time determined experimentally,
        #the I2C bus seems to timeout with anything less?)
        time.sleep(0.8)

    #0 = x1 gain, 1 = x3.7 gain, 2 = x16 gain, 3 = x64 gain
    def set_gain(self, gain):
        #Check that the requested gain is valid
        if gain in (0,1,2,3):
            #Fetch the current setup register state
            current_state = self.read_reg(AS7262_DEVICE_SETUP_REG)
            #Blank the bits controlling the gain, leave the rest as-is
            new_state = current_state & 0b11001111
            #The gain bits are no. 4 & 5, so shift gain to match
            gain = gain << 4
            #Add the new gain value to new_state
            new_state = new_state | gain
            #Write the new_state to the device
            self.write_reg(AS7262_DEVICE_SETUP_REG, new_state)
        else:
            print("Error! set_gain requires a value of 0-3. Value given was " + str(gain) + ".")

    #Function to set the integration time.  Takes a value between 1 and 255. This is
    # multiplied by 2.8 ms to give the integration time. Modes 0 an 1 require one
    #integration time to complete, modes 2 and 3 require two integration times.
    def set_integration_time(self,time):
        #Check that the requested time is valid
        if (255 >= time >= 1):
            #Write the integration time to the INT_T register (0x05)
            self.write_reg(AS7262_DEVICE_INT_T_REG, int(time))
        else:
            print("Error! set_integration_time requires a value of 1-255. Value given was " + str(time) + ".")
    pass # end of main class 


'''

if __name__ == "__main__":
    # Unit test : 
    # creating object of respected class 
    _obj = lightSensor_As7262()
    # reset the device first
    _obj.soft_reset()
    #Set the gain of the device between 0 and 3.  Higher gain = higher readings
    _obj.set_gain(3)
    #Set the integration time between 1 and 255.  Higher means longer readings
    _obj.set_integration_time(50)
    #Set the board to continuously measure all colours
    _obj.set_measurement_mode(2)
    try:
        _obj.enable_main_led()
        while True:
            # get clibrated values and store it in results list 
            results = _obj.get_calibrated_values()
            print("Red    :" + str(results[0]))
            print("Orange :" + str(results[1]))
            print("Yellow :" + str(results[2]))
            print("Green  :" + str(results[3]))
            print("Blue   :" + str(results[4]))
            print("Violet :" + str(results[5]) + "\n")
    except Exception as error:
        print(f"{error}")    '''