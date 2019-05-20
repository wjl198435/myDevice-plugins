import time
from feedrobot.weightsensors.hx711Class import hx711Class
from myDevices.utils.logger import error, debug
# from feedrobot.weight_sensors.Test import Test

class Food_Weight(hx711Class):
    def __init__(self,dout_pin=5, pd_sck_pin=6, file_name="5kg-food"):
        debug('dout_pin {0} pd_sck_pin{1} file_name {2}'.format(dout_pin,pd_sck_pin,file_name))
        hx711Class.__init__(self,dout_pin, pd_sck_pin, file_name)
    def __str__(self):
        return "Food Weight"

class Head_Weight(hx711Class):
    def __init__(self,dout_pin=21, pd_sck_pin=20, file_name="NA4-350kg-Head"):
        debug('dout_pin {0} pd_sck_pin{1} file_name {2}'.format(dout_pin,pd_sck_pin,file_name))
        hx711Class.__init__(self,dout_pin, pd_sck_pin, file_name)
    def __str__(self):
        return "Head Weight"  

class Tail_Weight(hx711Class):
    def __init__(self,dout_pin=23, pd_sck_pin=24, file_name="NA4-350kg-Tail"):
        debug('dout_pin {0} pd_sck_pin{1} file_name {2}'.format(dout_pin,pd_sck_pin,file_name))
        hx711Class.__init__(self,dout_pin, pd_sck_pin, file_name)
    def __str__(self):
        return "Tail Weight"          
# class weight(object):
#     def __init__(self):
#         print("begin body_front")
#         self.body_front = WeightHx711(dout_pin=21, pd_sck_pin=20, file_name="NA4-350kg-front")
#         time.sleep(1)
#         print("begin body_back")
#         self.body_back = WeightHx711(dout_pin=23, pd_sck_pin=24, file_name="NA4-350kg-back")
#         time.sleep(1)
#         self.food_weight =  WeightHx711(dout_pin=5, pd_sck_pin=6, file_name="5kg-food")

#     def get_body_weight(self):
#         if  self.body_front  and  self.body_back   :
            
#             front_weight = self.body_front.get_weight()
#             print("front_weight:", front_weight)
            
#             back_weight = self.body_back.get_weight()
#             print("back_weight:", back_weight)

#             total_weight = front_weight + back_weight
#             return total_weight
#         else:
#             return float(0.0)

#     def get_food_weight(self):
#         if self.food_weight :
#             return self.food_weight.get_weight()

#     def recalibration_body_weight(self, known_weight_grams=10):
#         if self.body_front :
#             self.body_front.reCalibration(known_weight_grams)
#         if self.body_back is not None:
#             self.body_back.reCalibration(known_weight_grams)

#     def recalibration_food_weight(self, known_weight_grams=10):
#         if  self.food_weight :
#             self.food_weight.reCalibration(known_weight_grams)



if __name__ == "__main__":

    food_weight = Food_Weight()
    print("body weight:",food_weight.get_weight())

    head_weight = Head_Weight()
    headWeight = head_weight.get_weight()
    print("Head weight:",headWeight)


    tail_weight = Tail_Weight()
    tailWeight = tail_weight.get_weight()
    print("Tail weight:",tailWeight)
    
    total=headWeight+tailWeight
    print('total:',total)
    
    # tw = Test()
    # print(tw.get_value())
