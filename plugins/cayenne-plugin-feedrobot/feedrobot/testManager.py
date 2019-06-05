from multiprocessing.managers import BaseManager, RemoteError
from myDevices.utils.logger import error, debug,info,setInfo,setDebug

SERVER_ADDRESS = ('127.0.0.1', 5600)
AUTH_KEY = b'abc'

class FeedRobotManager(BaseManager):
    """Manager for sharing Sense HAT data between processes."""
    pass

def connect_client():
    """Connect a client to the sensehat service."""
    try:
        debug('Connecting to sensehat service')        
        FeedRobotManager.register('Maths')
        # FeedRobotManager.register('use_emulator')
        FeedRobotManager.register('FeedRobotHub')
        manager = FeedRobotManager(SERVER_ADDRESS, AUTH_KEY)
        manager.connect()
        return manager
    except RemoteError as e:
        error('Error connecting to sensehat service, if using the Sense HAT emulator make sure it is has been launched in the GUI')



if __name__ == "__main__":
    setDebug()
    manager = connect_client()
    # manager.FeedRobotHub.digitalWrite(26,0)
    # print(manager.Maths().get_value())
    # print(manager.FeedRobotHub().digitalWrite(26,1))
    feed_robot = manager.FeedRobotHub()
    debug("Sensor body temp:{}".format(manager.FeedRobotHub().get_ir_body_temp()))
    debug("Sensor amb temp:{}".format(manager.FeedRobotHub().get_ir_amb_temp()))
    # debug("Sensor food weight:{}".format(manager.FeedRobotHub().get_food_weight()))
    # debug("Sensor body weight:{}".format(manager.FeedRobotHub().get_body_weight()))

    # hardware = manager.Hardware()
    # debug("hardware.getMac:{}".format(hardware.getMac()))

    # systemInfo = manager.SystemInfo()
    # debug("SystemInfo:{}".format(hardware.getMac()))
    # sysInfo = {item['channel']:item for item in systemInfo.getSystemInformation()}
    # info(sysInfo)