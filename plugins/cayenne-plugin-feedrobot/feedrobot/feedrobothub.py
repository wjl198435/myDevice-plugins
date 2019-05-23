import traceback
import sys
from myDevices.utils.logger import error, debug,info,setInfo,setDebug
from feedrobot.weightsensors.weight import (FoodWeightClass,HeadWeightClass,TailWeightClass)
from feedrobot.tempsensors.mlx90614  import MLX90614
from feedrobot.distancesensors.gp2y0e03 import GP2Y0E03

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
            return self._food_weight.get_weight()
        else:
            return -1    


    def _init_body_weight(self):
        debug("_init_body_weight ")
        """
        Internal. Initialises the food_weight sensor 
        """
        if not self._body_weight_init:
            try:
                self._head_body_weight = HeadWeightClass()
                self._tail_body_weight = TailWeightClass()
                self._body_weight_init = True
            except:
                error(traceback.print_exc())
    def get_body_weight(self):
        debug("get_body_weight ")
        self._init_body_weight()
        if self._body_weight_init:
            _head_body_weight = self._head_body_weight.get_weight()
            _tail_body_weight = self._tail_body_weight.get_weight()
            total_body_weight = _head_body_weight + _tail_body_weight
            debug("total_body_weight:{0}g head_body_weight:{1}g tail_body_weight:{2}g".format(total_body_weight,_head_body_weight,total_body_weight))
            return (total_body_weight)
        else :
            return -1    

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
            return self._ir_temp.get_obj_temp()
        else:
            return -100    

    def get_ir_amb_temp(self):
        debug("get_ir_amb_temp ")
        self._init_ir_temp()
        if self._ir_temp_init:
            return self._ir_temp.get_amb_temp()
        else:
            return -100  

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
            return self._body_dist.get_distance()
        else:
            return -1            
        

if __name__ == "__main__":
    setDebug()
    frh=FeedRobotHub()
    debug("food weight {0} g".format(frh.get_food_weight()))
    debug("body weight {0} g".format(frh.get_body_weight()))
   
    debug("ir_amb_temp:{}C".format(frh.get_ir_amb_temp()))
    debug("ir_body_temp:{}C".format(frh.get_ir_body_temp()))

    debug("get_body_dist:{} mm".format(frh.get_body_dist()))
 
