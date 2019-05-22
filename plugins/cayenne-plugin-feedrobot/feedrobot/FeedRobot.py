from myDevices.utils.logger import error, debug,info,setInfo,setDebug
from feedrobot.weightsensors.weight import (FoodWeightClass,HeadWeightClass,TailWeightClass)
class SenseHat(object):
    def __init__(self):
        self._food_weight = FoodWeightClass()
        self._food_weight_init = False 
   
   def _init_food_weight(self):
        """
        Internal. Initialises the food weight hx711 sensor 
        """
        if not self._food_weight_init:
            self._food_weight_init = self._food_weight 
            if not self._food_weight_init:
                raise OSError('Pressure Init Failed')    
