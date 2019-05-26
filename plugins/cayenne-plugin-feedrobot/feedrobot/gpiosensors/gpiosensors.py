import time
import unittest
from myDevices.utils.logger import exception, setDebug, info, debug, error, logToFile, setInfo
from myDevices.devices.digital.gpio import NativeGPIO

from feedrobot.config import (CONF_DOOR_ENTER_SWITCH_GPIO,CONF_DOOR_ENTER_STATUS_GPIO,
                              CONF_DOOR_EXIT_SWITCH_GPIO,CONF_DOOR_EXIT_STATUS_GPIO,
                              CONF_BUCKET_FORWARD_GPIO,CONF_BUCKET_REVERSE_GPIO)

class GPIOSensors(object):
    def __init__(self):
        self.gpio = NativeGPIO()
        self._door_enter_switch_gpio_init = False  
        self._door_exit_switch_gpio_init = False  
        self._door_enter_status_gpio_init = False  
        self._door_exit_status_gpio_init = False  

        self._bucket_forward_gpio_init = False
        self._bucket_forward_gpio_init = False
    
    def turn_on_door_enter_switch(self):
        if not self._door_enter_switch_gpio_init:
            function = self.gpio.setFunctionString(CONF_DOOR_ENTER_SWITCH_GPIO, 'OUT')   
            if function == 'UNKNOWN':
                error("Error Init Set pin {0} Function is {1}".format(CONF_DOOR_ENTER_SWITCH_GPIO,function))
                return {-1,function}
            else:
                debug("Ok Init set pin {0} Function is {1}".format(CONF_DOOR_ENTER_SWITCH_GPIO,function))
                self._door_enter_switch_gpio_init =True
        else :
            value = self.gpio.digitalWrite(pin, 1)
            return {0,value}
            
                   





# from myDevices.sensors import sensors
# from myDevices.devices import manager
# from myDevices.utils.logger import exception, setDebug, info, debug, error, logToFile, setInfo
# from myDevices.devices.bus import checkAllBus, BUSLIST
# from myDevices.devices import instance
# from time import sleep
# from json import loads, dumps
# from feedrobot.config import (CONF_DOOR_ENTER_GPIO,CONF_DOOR_EXIT_GPIO)

# gpio_sensors = {'enter_door_switch' : {'description': 'Enter  Door', 'device': 'RelaySwitch', 'args': {'gpio': 'GPIO', 'invert': False, 'channel': CONF_DOOR_ENTER_GPIO}, 'name': 'enter_door_relay'},
#                 'exit_door_switch' : {'description': 'Exit  Door', 'device': 'RelaySwitch', 'args': {'gpio': 'GPIO', 'invert': False, 'channel': CONF_DOOR_EXIT_GPIO}, 'name': 'exit_door_relay'}
#             # 'bucket_power_switch' : {'description': 'Bucket Power', 'device': 'MotorSwitch', 'args': {'gpio': 'GPIO', 'invert': False, 'channel': bucket_power_channel}, 'name': 'bucket_power_relay'},
#           }

# class GPIOSensors(object):
#     def __init__(self):
#         self.previousSystemData = None
#         self.currentSystemData = None
#         self.sensorsClient = sensors.SensorsClient()

#     def addSensors(self):
#         for sensor in gpio_sensors.values():
#             self.sensorsClient.AddSensor(sensor['name'], sensor['description'], sensor['device'], sensor['args'])


#     def setSensorValue(self, sensor, value):
#         self.sensorsClient.SensorCommand('integer', sensor['name'], None, value)
#         channel = 'dev:{}'.format(sensor['name'])
#         sensorInfo = next(obj for obj in self.sensorsClient.SensorsInfo() if obj['channel'] == channel)
#         return sensorInfo['value']
#         # self.assertEqual(value, sensorInfo['value'])

#     def setChannelFunction(self, channel, function):
#         self.sensorsClient.GpioCommand('function', channel, function)
#         bus = {item['channel']:item['value'] for item in self.sensorsClient.BusInfo()}
#         return bus['sys:gpio:{};function'.format(channel)]
#         # self.assertEqual(function, bus['sys:gpio:{};function'.format(channel)])

#     def setChannelValue(self, channel, value):
#         self.sensorsClient.GpioCommand('value', channel, value)
#         bus = {item['channel']:item['value'] for item in self.sensorsClient.BusInfo()}
#         return bus['sys:gpio:{};value'.format(channel)]
#         # self.assertEqual(value, bus['sys:gpio:{};value'.format(channel)]) 
#         #    
#     def listSensors(self):  
#         info('testListSensors')
#         deviceNames = [device for device in manager.getDeviceList()]
#         info(deviceNames)
#         return deviceNames

#     def removeSensor(self,name):
#         info('romoveSensor')
#         return self.sensorsClient.RemoveSensor(name)
#         # self.assertTrue(SensorsClientTest.client.RemoveSensor(name))    

#     def getSensorsInfo(self):
#         debug('getSensorsInfo')
#         sensors = self.sensorsClient.SensorsInfo()
#         info('Sensors info: {}'.format(sensors))
#         return sensors
#         # for sensor in sensors:
#         #     self.assertEqual('dev:', sensor['channel'][:4])
#         #     self.assertIn('value', sensor)  
     
#     def OnDataChanged(self, sensor_data):
#         # if len(sensor_data) < 5:
#         #     info('OnDataChanged: {}'.format(sensor_data))
#         # else:
#         #     info('OnDataChanged: {}'.format(len(sensor_data)))
#         self.previousSystemData = self.currentSystemData
#         self.currentSystemData = sensor_data
#         if self.previousSystemData:
#             self.done = True

#     def setSensorCallback(self):
#         debug('setSensorCallback')
#         self.done = False
#         self.sensorsClient.SetDataChanged(self.OnDataChanged)
       
#         items = [x for x in self.currentSystemData if x not in self.previousSystemData]
#         info('Changed items: {}'.format(items))
#         # self.assertNotEqual(self.previousSystemData, self.currentSystemData)
#         return items   
#     def removeAllSensors(self):
#         debug('removeAllSensors')
#         for sensor in gpio_sensors.values():
#             info(sensor)    


# if __name__ == '__main__':
#     setInfo()
#     gpios=GPIOSensors()
#     # info(gpiosensor.listSensors)
#     # gpios.setChannelValue()
#     gpios.removeAllSensors()
#     info(gpios.setSensorCallback)


#     sleep(10)
#     gpios.sensorsClient.StopMonitoring()
