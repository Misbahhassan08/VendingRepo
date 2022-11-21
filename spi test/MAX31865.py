import pigpio
from time import sleep 

class MAX31865:
    def __init__(self):
        self.pi1 = pigpio.pi()
        self.h = self.pi1.spi_open(0,50000,3)
        pass
    def _write_registers(self,regNum, dataByte):
        addressByte = 0x80 | regNum;
        self.pi1.spi_xfer(self.h,[addressByte])
        self.pi1.spi_xfer(self.h,dataByte)
        print(self.h)
    def _read_registers(self, regNumStart, numRegisters):
        data = None
        count = None
        count,data = self.pi1.spi_xfer(self.h,regNumStart)
        if count > 0 and count != None:
            print(self.h)
            return data
        
    def read_temp(self):
        self._write_registers(0x00,[0xA2])
        sleep(0.1)
        rtd = self._read_registers(b'\0x00',b'\0x08')
        #rtd_msb,rtd_lsb = rtd[1],rtd[2]
        #rtd_adc_code = (( rtd_msb << 0x08 ) | rtd_lsb ) >> 1
        print(rtd)
        
if __name__ == "__main__":
    rtd = MAX31865()
    rtd.read_temp()