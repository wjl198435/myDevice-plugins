
"""
This module provides script for starting the Sense HAT service. This service is needed so that it can be run
as root to use the sense_hat module, while allowing clients that are not running as root to access Sense HAT data.
"""
from myDevices.utils.logger import error, debug,info,setInfo,setDebug
from feedrobot.manager import start_server

if __name__ == "__main__":
    setDebug()
    start_server(True)
