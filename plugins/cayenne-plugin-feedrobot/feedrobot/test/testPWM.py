import RPi.GPIO as GPIO
import unittest

FOWARD_PIN = 17
RESVERSE_PIN = 25

class PWMTest(unittest.TestCase):
    def setUp(self):
        self.gpio = NativeGPIO()
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(FOWARD, GPIO.OUT)
        # GPIO.setup(RESVERSE, GPIO.OUT)
        foward_pin = self.gpio.setFunctionString(FOWARD_PIN, 'OUT')
        reverse_pin  = self.gpio.setFunctionString(RESVERSE_PIN, 'OUT')
        print("foward_pin")


        foward = GPIO.PWM(FOWARD, 0.8) 
        reverse = GPIO.PWM(RESVERSE, 0.8)    

    def foward_run(self):



if __name__ == '__main__':
