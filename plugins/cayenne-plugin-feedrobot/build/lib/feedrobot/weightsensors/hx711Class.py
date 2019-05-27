#!/usr/bin/env python3
import pickle
import os
import RPi.GPIO as GPIO  # import GPIO
# from hx711 import HX711  # import the class HX711
from feedrobot.weightsensors.hx711 import HX711

basename = '/etc/myDevices/plugins/cayenne-plugin-feedrobot/data/'
extension_name = '.swp'


class hx711Class(object):

    def __init__(self, dout_pin=21, pd_sck_pin=20, file_name="front"):
        self.swap_file_name = basename+file_name+extension_name
        print("self.swap_file_name-->",self.swap_file_name)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        try:
            GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
            # Create an object hx which represents your real hx711 chip
            # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
            self.hx = HX711(dout_pin, pd_sck_pin)
            # hx.__offset = 0
            # Check if we have swap file. If yes that suggest that the program was not
            # terminated proprly (power failure). We load the latest state.

            if os.path.isfile(self.swap_file_name):
                with open(self.swap_file_name, 'rb') as swap_file:
                    self.hx = pickle.load(swap_file)
                    # now we loaded the state before the Pi restarted.
            else:
                # measure tare and save the value as offset for current channel
                # and gain selected. That means channel A and gain 128
                err = self.hx.zero()
                # check if successful
                if err:
                    raise ValueError('Tare is unsuccessful.')

                reading = self.hx.get_raw_data_mean()
                if reading:  # always check if you get correct value or only False
                    # now the value is close to 0
                    print('Data subtracted by offset but still not converted to units:',
                          reading)
                else:
                    print('invalid data', reading)

                # In order to calculate the conversion ratio to some units, in my case I want grams,
                # you must have known weight.
                input('Put known weight on the scale and then press Enter')
                reading = self.hx.get_data_mean()
                if reading:
                    print('Mean value from HX711 subtracted by offset:', reading)
                    known_weight_grams = input(
                        'Write how many grams it was and press Enter: ')
                    try:
                        value = float(known_weight_grams)
                        print(value, 'grams')
                    except ValueError:
                        print('Expected integer or float and I have got:',
                              known_weight_grams)

                    # set scale ratio for particular channel and gain which is
                    # used to calculate the conversion to units. Required argument is only
                    # scale ratio. Without arguments 'channel' and 'gain_A' it sets
                    # the ratio for current channel and gain.
                    ratio = reading / value  # calculate the ratio for channel A and gain 128
                    self.hx.set_scale_ratio(ratio)  # set ratio for current channel
                    print('Ratio is set.')
                else:
                    raise ValueError(
                        'Cannot calculate mean value. Try debug mode. Variable reading:',
                        reading)

                # This is how you can save the ratio and offset in order to load it later.
                # If Raspberry Pi unexpectedly powers down, load the settings.
                print('Saving the HX711 state to swap file on persistant memory')
                with open(self.swap_file_name, 'wb') as swap_file:
                    pickle.dump(self.hx, swap_file)
                    swap_file.flush()
                    os.fsync(swap_file.fileno())
                    # you have to flush, fsynch and close the file all the time.
                    # This will write the file to the drive. It is slow but safe.

        except (KeyboardInterrupt, SystemExit):
            print('Bye :)')
        return None

    def reCalibration(self, known_weight_grams=10):
        err = self.hx.zero()
        # check if successful
        if err:
            raise ValueError('Tare is unsuccessful.')

        reading = self.hx.get_raw_data_mean()
        if reading:  # always check if you get correct value or only False
            # now the value is close to 0
            print('Data subtracted by offset but still not converted to units:',
                  reading)
        else:
            print('invalid data', reading)

        # In order to calculate the conversion ratio to some units, in my case I want grams,
        # you must have known weight.
        # input('Put known weight on the scale and then press Enter')
        reading = self.hx.get_data_mean()
        if reading:
            print('Mean value from HX711 subtracted by offset:', reading)
            # known_weight_grams = input(
            #     'Write how many grams it was and press Enter: ')
            try:
                value = float(known_weight_grams)
                print(value, 'grams')
            except ValueError:
                print('Expected integer or float and I have got:',
                      known_weight_grams)

            # set scale ratio for particular channel and gain which is
            # used to calculate the conversion to units. Required argument is only
            # scale ratio. Without arguments 'channel' and 'gain_A' it sets
            # the ratio for current channel and gain.
            ratio = reading / value  # calculate the ratio for channel A and gain 128
            self.hx.set_scale_ratio(ratio)  # set ratio for current channel
            print('Ratio is set.')
        else:
            raise ValueError(
                'Cannot calculate mean value. Try debug mode. Variable reading:',
                reading)

        # This is how you can save the ratio and offset in order to load it later.
        # If Raspberry Pi unexpectedly powers down, load the settings.
        print('Saving the HX711 state to swap file on persistant memory')
        with open(self.swap_file_name, 'wb') as swap_file:
            pickle.dump(self.hx, swap_file)
            swap_file.flush()
            os.fsync(swap_file.fileno())
            # you have to flush, fsynch and close the file all the time.
            # This will write the file to the drive. It is slow but safe.

    def get_weight(self):
         weight = round(abs(self.hx.get_weight_mean(20)), 2)
         return weight

    def close(self):
        pass

    def __del__(self):
        GPIO.cleanup()

if __name__ == "__main__":

    """ p21 p2"""
#    weight1 = WeightHx711(dout_pin=21, pd_sck_pin=20,file_name="front")
#    weight1.reCalibration()
#    print(weight1.get_weight())

    # weight2 = WeightHx711(dout_pin=23, pd_sck_pin=24, file_name="back")
    # print(weight2.get_weight())
 
    foodWeight = hx711Class(dout_pin=5, pd_sck_pin=6, file_name="5kg-food")
    print(foodWeight.get_weight())
    GPIO.cleanup()

