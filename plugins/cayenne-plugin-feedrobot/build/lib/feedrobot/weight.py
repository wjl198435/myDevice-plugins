
from feedrobot.WeightHx711 import WeightHx711


class Weight(object):
    def __init__(self):
        self.body_front = WeightHx711(dout_pin=21, pd_sck_pin=20, file_name="front")
        self.body_back = WeightHx711(dout_pin=23, pd_sck_pin=24, file_name="back")
        self.food_weight = None

    def get_body_weight(self):
        if self.body_front is not None and self.body_back is not None:
            front_weight = self.body_front.get_weight()
            back_weight = self.body_back.get_weight()
            print("front_weight", front_weight)
            print("back_weight", back_weight)
            total_weight = front_weight + back_weight
            return total_weight
        else:
            return float(0.0)

    def get_food_weight(self):
        if self.food_weight is not None:
            return self.food_weight.get_weight()

    def recalibration_body_weight(self, known_weight_grams=10):
        if self.body_front is not None:
            self.body_front.reCalibration(known_weight_grams)
        if self.body_back is not None:
            self.body_back.reCalibration(known_weight_grams)

    def recalibration_food_weight(self, known_weight_grams=10):
        if self.food_weight is not None:
            self.food_weight.reCalibration(known_weight_grams)



if __name__ == "__main__":

    weight = Weight()

    print(weight.get_body_weight())