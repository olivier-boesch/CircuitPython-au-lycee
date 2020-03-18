import board
from i2c_device import I2CDevice

# ---- registers
REG_HUM_LSB = 0xFE
REG_HUM_MSB = 0xFD
REG_TEMP_XLSB = 0xFC
REG_TEMP_LSB = 0xFB
REG_TEMP_MSB = 0xFA
REG_PRESS_XLSB = 0xF9
REG_PRESS_LSB = 0xF8
REG_PRESS_MSB = 0xF7
REG_CONFIG = 0xF5
REG_CTRL_MEAS = 0xF4
REG_STATUS = 0xF3
REG_CTRL_HUM = 0xF2
REGS_CALIB2641 = [0xE1,0xF0]
REGS_CALIB0025 = [0x88,0xA1]
REG_RESET = 0xE0
REG_ID = 0xD0

# ---- settings
SETTING_RESET = 0xB6

SETTING_MODE_SLEEP = 0x00
SETTING_MODE_FORCED = 0x10  # or 0x01
SETTING_MODE_NORMAL = 0x11

SETTING_OVERSAMPLING_NO = 0x00
SETTING_OVERSAMPLING_x1 = 0x01
SETTING_OVERSAMPLING_x2 = 0x02
SETTING_OVERSAMPLING_x4 = 0x03
SETTING_OVERSAMPLING_x8 = 0x04
SETTING_OVERSAMPLING_x16 = 0x05

SETTING_STANDBY_TIME_0_5MS = 0x00
SETTING_STANDBY_TIME_62_5MS = 0x01
SETTING_STANDBY_TIME_125MS = 0x02
SETTING_STANDBY_TIME_250MS = 0x03
SETTING_STANDBY_TIME_500MS = 0x04
SETTING_STANDBY_TIME_1000MS = 0x05
SETTING_STANDBY_TIME_10MS = 0x06
SETTING_STANDBY_TIME_20MS = 0x07

SETTING_FILTER_OFF = 0x00
SETTING_FILTER_2 = 0x01
SETTING_FILTER_4 = 0x02
SETTING_FILTER_8 = 0x03
SETTING_FILTER_16 = 0x04



class Bme280(I2CDevice):
    def __init__(self, i2c, device_address=0x76, probe=True):
        super().__init__(i2c, device_address, probe=True)
        self.config_device()
        
    def reset(self):
        self.write(bytes([REG_RESET, SETTING_RESET]))
        
    def config_device(self):
        pass
    
    @property
    def temperature(self):
        pass
    
    @property    
    def humidity(self):
        pass
    
    @property
    def pressure(self):
        pass
