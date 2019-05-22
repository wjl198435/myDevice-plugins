"""
This module provides a functions for starting and connecting to a Sense HAT service. This service is needed so that it can be run
as root to use the sense_hat module, while allowing clients that are not running as root to access Sense HAT data.
"""
from multiprocessing.managers import BaseManager, RemoteError
from myDevices.utils.logger import error, debug
from feedrobot.demo import MathsClass
from feedrobot import FeedRobot

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
    FeedRobotManager.register('Maths', MathsClass)
    FeedRobotManager.register('FeedRobot', FeedRobot)
    manager = FeedRobotManager(address=SERVER_ADDRESS, authkey=AUTH_KEY)
    manager.get_server().serve_forever()

def connect_client():
    """Connect a client to the feedrobot service."""
    try:
        debug('Connecting to feedrobot service')
        FeedRobotManager.register('Maths', MathsClass)
        FeedRobotManager.register('FeedRobot',FeedRobot)
        manager = FeedRobotManager(address=SERVER_ADDRESS, authkey=AUTH_KEY)
        manager.connect()
        return manager
    except RemoteError as e:
        error('Error connecting to feedrobot service, if using the Sense HAT emulator make sure it is has been launched in the GUI')

if __name__ == "__main__":
    manager = connect_client()
    # print(manager.Maths.get_value())
    # print(manager.FeedRobot)

