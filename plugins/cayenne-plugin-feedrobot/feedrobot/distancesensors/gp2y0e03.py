import smbus
import time
from myDevices.utils.logger import error, debug,info,setInfo,setDebug
_REGISTER_SHIFT_BIT = 0x35
_REGISTER_DISTANCE = 0x5e

class GP2Y0E03:
    def __init__(self, bus_num=1, address=0x29):
        self.bus_num = 1
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)

    def _register8(self, register, value=None):
        return self.bus.read_byte_data(self.address, register)

    def _register16(self, register, value=None):
        return self.bus.read_i2c_block_data(self.address, register,2)

    def get_distance(self, raw=False):
        shift = self._register8(_REGISTER_SHIFT_BIT)
        value = self._register16(_REGISTER_DISTANCE)
        # debug('shift {0} value {1}'.format(shift, value))
        dist = (((value[0] << 4) + value[1])/float(16))/float(2**shift) 
        return dist

if __name__ == "__main__":
    setDebug()
    s = GP2Y0E03()
    while True:
        print(s.get_distance())
        time.sleep(1.5)