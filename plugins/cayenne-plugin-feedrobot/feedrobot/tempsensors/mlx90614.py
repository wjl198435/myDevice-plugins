import smbus
from time import sleep
from myDevices.utils.logger import error, debug,info,setInfo,setDebug

class MLX90614(object):
    def __init__(self, address=0x5a, bus_num=1):
        
        self.bus_num = bus_num
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)

        self.MLX90614_RAWIR1=0x04
        self.MLX90614_RAWIR2=0x05
        self.MLX90614_TA=0x06
        self.MLX90614_TOBJ1=0x07
        self.MLX90614_TOBJ2=0x08

        self.MLX90614_TOMAX=0x20
        self.MLX90614_TOMIN=0x21
        self.MLX90614_PWMCTRL=0x22
        self.MLX90614_TARANGE=0x23
        self.MLX90614_EMISS=0x24
        self.MLX90614_CONFIG=0x25
        self.MLX90614_ADDR=0x0E
        self.MLX90614_ID1=0x3C
        self.MLX90614_ID2=0x3D
        self.MLX90614_ID3=0x3E
        self.MLX90614_ID4=0x3F

        self.comm_retries = 1
        self.comm_sleep_amount = 0.1
    
    def __str__(self):
        return "MLX90614" 

    def read_reg(self, reg_addr):
        for i in range(self.comm_retries):
            try:
                return self.bus.read_word_data(self.address, reg_addr)
            except IOError as e:
                # "Rate limiting" - sleeping to prevent problems with sensor
                # when requesting data too quickly
                sleep(self.comm_sleep_amount)
        # By this time, we made a couple requests and the sensor didn't respond
        # (judging by the fact we haven't returned from this function yet)
        # So let's just re-raise the last IOError we got
        raise e  

    def get_amb_temp(self):
        data = self.read_reg(self.MLX90614_TA)
        return self.data_to_temp(data)
        
    def get_obj_temp(self):
        data = self.read_reg(self.MLX90614_TOBJ1)
        return self.data_to_temp(data)    
        
    def data_to_temp(self, data):
        temp = (data*0.02) - 273.15
        return abs(round(temp,2))

if __name__ == "__main__":
    
    sensor = MLX90614()
    print(sensor.get_amb_temp())
    print(sensor.get_obj_temp())