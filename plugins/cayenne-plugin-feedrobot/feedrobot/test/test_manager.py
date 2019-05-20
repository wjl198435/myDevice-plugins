import os
from multiprocessing.managers import RemoteError
from myDevices.utils.logger import error, exception, info
from feedrobot.manager import connect_client
SERVER_ADDRESS = ('127.0.0.1', 5600)
AUTH_KEY = b'abc'

class TestManager(object):
    def __init__(self):
        self.manager = connect_client()
        # print(manager.Maths.get_value)
        self.Maths = self.manager.Maths()
    def get_value(self):
        return self.Maths.get_value()

if __name__ == "__main__":
    tm = TestManager() 
    print(tm.get_value())
    # print(.Maths.get_value)      
