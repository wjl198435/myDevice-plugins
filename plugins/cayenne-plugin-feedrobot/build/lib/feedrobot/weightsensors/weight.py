import time
from feedrobot.weightsensors.hx711Class import hx711Class
from myDevices.utils.logger import error, debug
from feedrobot.config import (CONF_WEIGHT_FOOD_GPIO_CK,CONF_WEIGHT_FOOD_GPIO_DO,CONF_WEIGHT_FOOD_SWAP_FILE,
                              CONF_WEIGHT_HEAD_GPIO_CK,CONF_WEIGHT_HEAD_GPIO_DO,CONF_WEIGHT_HEAD_SWAP_FILE,
                              CONF_WEIGHT_TAIL_GPIO_CK,CONF_WEIGHT_TAIL_GPIO_DO,CONF_WEIGHT_TAIL_SWAP_FILE)

class FoodWeightClass(hx711Class):
    def __init__(self,dout_pin=CONF_WEIGHT_FOOD_GPIO_DO, pd_sck_pin=CONF_WEIGHT_FOOD_GPIO_CK, file_name=CONF_WEIGHT_FOOD_SWAP_FILE):
        debug('dout_pin {0} pd_sck_pin{1} file_name {2}'.format(dout_pin,pd_sck_pin,file_name))
        hx711Class.__init__(self,dout_pin, pd_sck_pin, file_name)
    def __str__(self):
        return "Food Weight"

class HeadWeightClass(hx711Class):
    def __init__(self,dout_pin=CONF_WEIGHT_HEAD_GPIO_DO, pd_sck_pin=CONF_WEIGHT_HEAD_GPIO_CK, file_name=CONF_WEIGHT_HEAD_SWAP_FILE):
        debug('dout_pin {0} pd_sck_pin{1} file_name {2}'.format(dout_pin,pd_sck_pin,file_name))
        hx711Class.__init__(self,dout_pin, pd_sck_pin, file_name)
    def __str__(self):
        return "Head Weight"  

class TailWeightClass(hx711Class):
    def __init__(self,dout_pin=CONF_WEIGHT_TAIL_GPIO_DO, pd_sck_pin=CONF_WEIGHT_TAIL_GPIO_CK, file_name=CONF_WEIGHT_TAIL_SWAP_FILE):
        debug('dout_pin {0} pd_sck_pin{1} file_name {2}'.format(dout_pin,pd_sck_pin,file_name))
        hx711Class.__init__(self,dout_pin, pd_sck_pin, file_name)
    def __str__(self):
        return "Tail Weight"          

if __name__ == "__main__":

    food_weight = FoodWeightClass()
    print("food weight:",food_weight.get_weight())

    # head_weight = HeadWeightClass()
    # headWeight = head_weight.get_weight()
    # print("Head weight:",headWeight)

    # tail_weight = TailWeightClass()
    # tailWeight = tail_weight.get_weight()
    # print("Tail weight:",tailWeight)
    
    # total=headWeight+tailWeight
    # print('total:',total)
    

