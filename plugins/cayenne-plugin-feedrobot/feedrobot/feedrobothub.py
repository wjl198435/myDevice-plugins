import traceback
import sys
from myDevices.utils.logger import error, debug,info,setInfo,setDebug
from feedrobot.weightsensors.weight import (FoodWeightClass,HeadWeightClass,TailWeightClass,BodyWeightClass)
from feedrobot.tempsensors.mlx90614  import MLX90614
from feedrobot.distancesensors.gp2y0e03 import GP2Y0E03
from myDevices.devices.digital.gpio import NativeGPIO

from feedrobot.config import (CONF_DOOR_ENTER_SWITCH_GPIO,CONF_DOOR_ENTER_STATUS_GPIO,
                              CONF_DOOR_EXIT_SWITCH_GPIO,CONF_DOOR_EXIT_STATUS_GPIO,
                              CONF_BUCKET_FORWARD_GPIO,CONF_BUCKET_REVERSE_GPIO)


                             

SUPPORT_FOOD_WEIGHT = 1
SUPPORT_HEAD_WEIGHT = 2
SUPPORT_TAIL_WEIGHT = 4
SUPPORT_DOOR_SWITCH = 8
SUPPORT_TEMPERATURE = 16
SUPPORT_DISTANCE = 32
SUPPORT_DC_MOTOR = 64
SUPPORT_STATUS = 128
# SUPPORT_SEND_COMMAND = 256
# SUPPORT_LOCATE = 512
# SUPPORT_CLEAN_SPOT = 1024
# SUPPORT_MAP = 2048
# SUPPORT_STATE = 4096
# SUPPORT_START = 8192



SUPPORT_FEED_ROBOT = SUPPORT_FOOD_WEIGHT | SUPPORT_HEAD_WEIGHT | SUPPORT_TAIL_WEIGHT \
                    | SUPPORT_DOOR_SWITCH | SUPPORT_TEMPERATURE | SUPPORT_DISTANCE \
                    | SUPPORT_DC_MOTOR | SUPPORT_STATUS    



class FeedRobotHub(object):
    def __init__(self,support_food_weight=True,head_weight=True,
                tail_weight=True,door_switch=True,temperature=True,
                distance=True,dc_motor=True):
        debug("FeedRobotHat __init__")

        self._food_weight = None
        self._food_weight_init = False  # Will be initialised as and when needed

        self._body_weight = None
        self._body_weight_init = False  # Will be initialised as and when needed
        self._head_body_weight = None
        self._tail_body_weight = None

        self._ir_temp = None  # Will be initialised as and when needed
        self._ir_temp_init= False

        self._body_dist = None  # Will be initialised as and when needed
        self._body_dist_init= False

        # self.gpio = NativeGPIO()
        self._gpio = None
        self._gpio_init = False
        self.callback_data = 0

    def support(self):
        return SUPPORT_FEED_ROBOT
   
    def _init_food_weight(self):
        debug("_init_food_weight ")
        """
        Internal. Initialises the food_weight sensor 
        """
        if not self._food_weight_init:
            try:
                self._food_weight = FoodWeightClass()
                self._food_weight_init = True
            except:
                error(traceback.print_exc())
    def get_food_weight(self):
        debug("get_food_weight ")
        self._init_food_weight()
        if self._food_weight_init:
            value = self._food_weight.get_weight()
            return (0, "OK", value)
        else:
            return {-1,'error', 'Sensor Init error'}  


    def _init_body_weight(self):
        debug("_init_body_weight ")
        """
        Internal. Initialises the food_weight sensor 
        """
        if not self._body_weight_init:
            try:
                # self._head_body_weight = HeadWeightClass()
                # self._tail_body_weight = TailWeightClass()
                self._body_weight = BodyWeightClass()
                self._body_weight_init = True
            except:
                error(traceback.print_exc())
    def get_body_weight(self):
        debug("get_body_weight ")
        self._init_body_weight()
        if self._body_weight_init:
            # _head_body_weight = self._head_body_weight.get_weight()
            # _tail_body_weight = self._tail_body_weight.get_weight()
            # total_body_weight = _head_body_weight + _tail_body_weight
            total_body_weight = self._body_weight.get_weight()
            debug("total_body_weight:{0}g".format(total_body_weight))
            return (0, "OK", total_body_weight)
        else :
            return {-1,'error', 'Sensor Init error'} 

    def _init_ir_temp(self):
        debug("_init_ir_temp ")
        """
        Internal. Initialises the _init_ir_temp sensor 
        """
        if not self._ir_temp_init:
            try:
                self._ir_temp = MLX90614()
                self._ir_temp_init = True
            except:
                error(traceback.print_exc())

    def get_ir_body_temp(self):
        debug("get_ir_body_temp ")
        self._init_ir_temp()
        if self._ir_temp_init:
            return  (0, "OK", self._ir_temp.get_obj_temp())
        else:
            return (-1,'error','device init error')   

    def get_ir_amb_temp(self):
        debug("get_ir_amb_temp ")
        self._init_ir_temp()
        if self._ir_temp_init:
            return (0, "OK",  self._ir_temp.get_amb_temp())
        else:
            return (-1,'error','device init error')  

    def _init__body_dist(self):
        debug("_init_food_weight ")
        """
        Internal. Initialises the food_weight sensor 
        """
        if not self._body_dist_init:
            try:
                self._body_dist = GP2Y0E03()
                self._body_dist_init = True
            except:
                error(traceback.print_exc())
    def get_body_dist(self):
        debug("get_food_weight ")
        self._init__body_dist()
        if self._body_dist_init:
            value = self._body_dist.get_distance()
            return  (0, "OK", value)
        else:
            return  (-1,'error','device init error')   
    
    def edgeCallback(self, data, value):
        info('edgeCallback data {}, value {}'.format(data, value))
        self.callback_data = data

    def _initStatusCallback(self): 
        debug("_initStatusCallback ")
        pins_status_list = [CONF_DOOR_ENTER_STATUS_GPIO,CONF_DOOR_EXIT_STATUS_GPIO]
        for pin in pins_status_list:
            self.gpio.setFunctionString(pin, 'IN')
            self.gpio.setCallback(pin, self.edgeCallback, pin)
            
    def init_gpio(self):
        debug("_init_gpio ")
        if not self._gpio_init:
            self.gpio = NativeGPIO()
            self._gpio_init = True
            # self._initStatusCallback()
            # self._gpio_init = True
           
            # pins_out_list = [CONF_DOOR_ENTER_SWITCH_GPIO,CONF_DOOR_EXIT_SWITCH_GPIO,
            # CONF_BUCKET_FORWARD_GPIO,CONF_BUCKET_REVERSE_GPIO]
            
            # for pin in pins_out_list:
            #     function = self.gpio.setFunctionString(pin, 'OUT') 
            #     if function == 'UNKNOWN':
            #         error('Pin {} function UNKNOWN, skipping'.format(pin))  
        info("success init gpio")         


    def digitalWrite(self,channel, value):
        debug("_init_gpio channel:{0}, value:{1} ".format(channel, value))
        if not self._gpio_init:
            self.init_gpio()
        try:
            function = self.gpio.setFunctionString(channel, 'OUT')   
            debug("setFunctionString:{0},function:{1}".format(channel,function))
        
            pin_value = self.gpio.digitalWrite(channel, value) 
            debug("pin_value:{}".format(pin_value))
        
            if pin_value  == value:
                return  (0, "OK", value)
            else:
                return  (-1, "error", value)  
        except ValueError as ve:
            return  (-1, "error", value) 

    def get_condition_status(self):
        debug("get_amb_statu")
        
        cond_status = ConditionStatus()
        cond_status.temperature = self.get_ir_amb_temp()
        cond_status.food_weight =  self.get_food_weight()
        return cond_status


    def get_body_status(self):
        debug("get_body_status")
        body_status = BodyStatus()
        body_status.body_distance = self.get_body_dist()
        body_status.body_weight = self.get_body_weight()
        body_status.temperature = self.get_ir_body_temp()
        
        return body_status

       
    
class ConditionStatus(object):
    def __init__(self):
        self.temperature = 0
        self.food_weight = 0
    def __str__(self) -> str:
        """Represent body as string."""
        return ":temperature:{},food_weight:{}".format(self.temperature, self.food_weight)


    

class BodyStatus(object):
    def __init__(self):
        self.temperature = 0
        self.body_weight = 0
        self.body_distance= 0
    def __str__(self) -> str:
        """Represent body as string."""
        return ":temperature:{}, body_weight:{},body_distance:{}".format(self.temperature, self.body_weight,self.body_distance )






       
        
if __name__ == "__main__":
    setDebug()
    frh=FeedRobotHub()
    debug("body status{}".format(frh.get_condition_status()))
    debug("body status{}".format(frh.get_body_status()))
    # frh.get_body_status
    # debug("food weight {0} g".format(frh.get_food_weight()))
    # debug("body weight {0} g".format(frh.get_body_weight()))
   
    # debug("ir_amb_temp:{}C".format(frh.get_ir_amb_temp()))
    # debug("ir_body_temp:{}C".format(frh.get_ir_body_temp()))

    # debug("get_body_dist:{} mm".format(frh.get_body_dist()))
    # gpio_out_list = [CONF_DOOR_ENTER_SWITCH_GPIO,CONF_DOOR_EXIT_SWITCH_GPIO,
    # CONF_BUCKET_FORWARD_GPIO,CONF_BUCKET_REVERSE_GPIO]

    # gpio_status_list = [CONF_DOOR_ENTER_STATUS_GPIO,CONF_DOOR_EXIT_STATUS_GPIO]
    # for gpio in gpio_out_list:
    #     info(gpio)
    # for gpio in gpio_status_list:
    #     info(gpio)    
    # frh.init_gpio()
    # debug(":digitalWrite {}".format(frh.digitalWrite(27,0)))
   
 
