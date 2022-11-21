"""
All global varibles and json here
"""

# ---------------------------------------------------- MCP4541 globals ----------------------------------------------------------
"""
From page page37
 Address	Function				Memory Type
 00h 		Volatile Wiper 0 		RAM
 01h 		Volatile Wiper 1 		RAM
 02h 		Nonvolatile Wiper 0		EEPROM
 03h 		Nonvolatile Wiper 1		EEPROM
 04h 		Volatile TCON Register 	RAM
 05h 		Status Register 		RAM
 06h 		Data EEPROM 			EEPROM
 07h 		Data EEPROM 			EEPROM
 08h 		Data EEPROM 			EEPROM
 09h 		Data EEPROM 			EEPROM
 0Ah 		Data EEPROM 			EEPROM
 0Bh 		Data EEPROM 			EEPROM
 0Ch 		Data EEPROM 			EEPROM
 0Dh 		Data EEPROM 			EEPROM
 0Eh 		Data EEPROM 			EEPROM
 0Fh 		Data EEPROM 			EEPROM

"""

#TCON Reg bit constants
MCP4541_TERM_R0B = 0x0001
MCP4541_TERM_R0W = 0x0002
MCP4541_TERM_R0A = 0x0004
MCP4541_TERM_R0HW = 0x0008
MCP4541_TERM_R1B = 0x0010 # Not applicable for the MCP4561
MCP4541_TERM_R1W = 0x0020 # Not applicable for the MCP4561
MCP4541_TERM_R1A = 0x0040 # Not applicable for the MCP4561
MCP4541_TERM_R1HW = 0x0080 # Not applicable for the MCP4561
MCP4541_TCON_GCEN_BIT = 0x0100

MCP4541_VOL_WIPER_0 =    0x00
MCP4541_VOL_WIPER_1 =    0x01 # Not applicable for the MCP4561
MCP4541_NON_VOL_WIPER_0 = 0x02
MCP4541_NON_VOL_WIPER_1 = 0x03 # Not applicable for the MCP4561
MCP4541_TCON_REG    =   0x04
MCP4541_STATUS_REG  =    0x05

# The MCP4541 has 7 and MCP4561 has 10 General Purpose 9 bit wide 0x000 (0) - 0x1FF (511) 
# EEPROM Non-Volatile registers These registers come factory set to 0x0FF
MCP4541_GP_EEPROM_0  =   0x06
MCP4541_GP_EEPROM_1  =   0x07
MCP4541_GP_EEPROM_2  =   0x08
MCP4541_GP_EEPROM_3  =   0x09
MCP4541_GP_EEPROM_4  =   0x0A
MCP4541_GP_EEPROM_5  =   0x0B
MCP4541_GP_EEPROM_6  =   0x0C
MCP4541_GP_EEPROM_7  =   0x0D
MCP4541_GP_EEPROM_8  =   0x0E
MCP4541_GP_EEPROM_9  =   0x0F


MCP4541_WIPER_0    =     0x00
MCP4541_WIPER_1    =     0x01 # Not applicable for the MCP4561

MCP4541_ERR  	=	    0x0FFF
MCP4541_SUCCESS	=	    0x0000

# I2C Address default assumes Pin1 tied low to 0v. ie. A0 = 0.
# See Table 6-2 pp50 MCP4541 Microchip data sheet
# So A0 = 0 : B00101110, 46, 0x2E
#    A0 = 1 : B00101111, 47, 0x2F
MCP4541_DEFAULT_ADDRESS = 0x2E # check/verify this address with terminal command 


MCP4541_CMD_BYTE_WRITE_DATA = 0x00 #0
MCP4541_CMD_BYTE_INCREMENT  = 0x04 #4
MCP4541_CMD_BYTE_DECREMENT  = 0x08 #8
MCP4541_CMD_BYTE_READ_DATA  = 0x0C #12


u16Result = 0;
MAX_MESSAGE_SIZE = 150
MCP4541_MAX_REG_VAL = 0x01FF # See Table 7-2, Page pp56, note 1


MCP4541_ERR   = 0x0FFF
MCP4541_SUCCESS = 0x0000
MCP4541_bus_ADD = 0


#--------------------------------------------  AS7262 ---------------------------------------------------------------------

AS7262_Default_address = 0x49
AS7262_DEVICE_STATUS_REG = 0x00
AS7262_DEVICE_WRITE_REG = 0x01
AS7262_DEVICE_LED = 0x07
AS7262_DEVICE_SETUP_REG = 0x04
AS7262_DEVICE_INT_T_REG = 0x05
AS7262_bus_ADD = 1


# ---------------------------------------- Mux 9548A ------------------------------------------------------------------------ 

TCA9548A_I2C_address    = 0x70
TCA9548A_I2C_bus_number = 1

