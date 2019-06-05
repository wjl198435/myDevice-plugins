"""
This module provides a functions for starting and connecting to a Sense HAT service. This service is needed so that it can be run
as root to use the sense_hat module, while allowing clients that are not running as root to access Sense HAT data.
"""
from multiprocessing.managers import BaseManager, RemoteError
from myDevices.utils.logger import error, debug,info,setInfo,setDebug

from myDevices.system.hardware import Hardware, BOARD_REVISION, CPU_REVISION, CPU_HARDWARE 
from feedrobot.demo import MathsClass
from feedrobothub import FeedRobotHub
from myDevices.system.systeminfo import SystemInfo

SERVER_ADDRESS = ('127.0.0.1', 5600)
AUTH_KEY = b'abc'

class FeedRobotManager(BaseManager):
    """Manager for sharing Sense HAT data between processes."""
    pass

def start_server(emulate=False):
    """Start the feedrobot service.
    
    Arguments:
    emulate: True if the Sense HAT Emulator should be used. This requires the Emulator to be installed and running on the desktop. 
    """
    # SenseHATManager.register('SenseHat', SenseHat)
    # ('Maths', MathsClass)
    debug('start_server')
    FeedRobotManager.register('Maths', MathsClass)
    FeedRobotManager.register('FeedRobotHub', FeedRobotHub)
    FeedRobotManager.register('Hardware', Hardware)
    FeedRobotManager.register('SystemInfo', SystemInfo)
    SystemInfo
    manager = FeedRobotManager(address=SERVER_ADDRESS, authkey=AUTH_KEY)
    manager.get_server().serve_forever()

def connect_client():
    """Connect a client to the feedrobot service."""
    try:
        debug('Connecting to feedrobot service')
        FeedRobotManager.register('Maths', MathsClass)
        FeedRobotManager.register('FeedRobotHub',FeedRobotHub)
        FeedRobotManager.register('Hardware', Hardware)
        FeedRobotManager.register('SystemInfo', SystemInfo)
        manager = FeedRobotManager(address=SERVER_ADDRESS, authkey=AUTH_KEY)
        manager.connect()
        return manager
    except RemoteError as e:
        error('Error connecting to feedrobot service, if using the Sense HAT emulator make sure it is has been launched in the GUI')

if __name__ == "__main__":
    setDebug()
    manager = connect_client()
    # manager.FeedRobotHub.digitalWrite(26,0)
    # print(manager.Maths().get_value())
    # print(manager.FeedRobotHub().digitalWrite(26,1))
    # feed_robot = manager.FeedRobotHub()
    # debug("Sensor body temp:{}".format(manager.FeedRobotHub().get_ir_body_temp()))
    # debug("Sensor amb temp:{}".format(manager.FeedRobotHub().get_ir_amb_temp()))
    # debug("Sensor food weight:{}".format(manager.FeedRobotHub().get_food_weight()))
    # debug("Sensor body weight:{}".format(manager.FeedRobotHub().get_body_weight()))

    hardware = manager.Hardware()
    debug("hardware.getMac:{}".format(hardware.getMac()))

    systemInfo = manager.SystemInfo()
    debug("SystemInfo:{}".format(hardware.getMac()))
    self.info = {item['channel']:item for item in systemInfo.getSystemInformation()}
    info(self.info)
    # debug("Sensor body weight:{}".format(hardware.getMac()))
    
    # feed_robot.get_ir_body_temp()
    # debug(feed_robot.get_ir_body_temp())

