import time
import unittest
from myDevices.utils.logger import exception, setDebug, info, debug, error, logToFile, setInfo
from myDevices.devices.digital.gpio import NativeGPIO
from time import sleep
FOWARD_PIN = 12
RESVERSE_PIN = 25

class GpioTest(unittest.TestCase):
    def setUp(self):
        self.gpio = NativeGPIO()

    def testMotoFoward(self):
        info("testMotoFoward  Enter")
        forward_pin = self.gpio.setFunctionString(FOWARD_PIN, 'OUT')
        value = self.gpio.digitalWrite(FOWARD_PIN, 1)
        sleep(5)
        value = self.gpio.digitalWrite(FOWARD_PIN, 0)
        info("testMotoFoward Exit")
    
    def testSleep(slef):
        info("testSleep Enter")
        sleep(5)    
        info("testSleep Exit")

    def testMotoRevser(self):
        info("testMotoRevser  Enter")
        resver_pin = self.gpio.setFunctionString(RESVERSE_PIN, 'OUT')
        value = self.gpio.digitalWrite(RESVERSE_PIN, 1)
        sleep(5)
        value = self.gpio.digitalWrite(RESVERSE_PIN, 0) 
        info("testMotoRevser Exit")   


    def testGPIO(self):

        pins = []
        for header in self.gpio.MAPPING:
            pins.extend([pin['gpio'] for pin in header['map'] if 'gpio' in pin and 'alt0' not in pin and 'overlay' not in pin])
        for pin in pins:
            info('Testing pin {}'.format(pin))
            function = self.gpio.setFunctionString(pin, 'OUT')
            if function == 'UNKNOWN':
                info('Pin {} function UNKNOWN, skipping'.format(pin))
                continue
            self.assertEqual('OUT', function)
            value = self.gpio.digitalWrite(pin, 1)
            self.assertEqual(value, 1)
            value = self.gpio.digitalWrite(pin, 0)
            self.assertEqual(value, 0)

    def testPinStatus(self):
        pin_status = self.gpio.wildcard()
        info(pin_status)
        self.assertEqual(set(self.gpio.pins + self.gpio.overlay_pins), set(pin_status.keys()))
        for key, value in pin_status.items():
            self.assertCountEqual(value.keys(), ('function', 'value'))
            if key in self.gpio.pins:
                self.assertGreaterEqual(value['value'], 0)
                self.assertLessEqual(value['value'], 1)

    def edgeCallback(self, data, value):
        info('edgeCallback data {}, value {}'.format(data, value))
        self.callback_data = data

    def testEdgeCallback(self):
        self.callback_data = 0
        pin = 25
        self.gpio.setFunctionString(pin, 'IN')
        self.gpio.setCallback(pin, self.edgeCallback, pin)
        for x in range(15):
            if self.callback_data != 0:
                break
            time.sleep(1)
        self.assertEqual(pin, self.callback_data)


if __name__ == '__main__':
    setInfo()

    while True:
        tests=[
            GpioTest("testMotoFoward"),
            GpioTest("testSleep"),
            GpioTest("testMotoRevser")
        ]

        suite = unittest.TestSuite()
        suite.addTests(tests)
    
        runner =  unittest.TextTestRunner()
        runner.run(suite)
   
    # unittest.main()

    # while True:
    #     testMotoFoward()
    #     sleep(1)
    #     testMotoRevser()

