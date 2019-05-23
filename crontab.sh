#!/bin/bash
#
# myDevices watchdog

SERVICE=service
GREP=/bin/grep
PS=/bin/ps
NOP=/bin/true
DATE=/bin/date

. /lib/lsb/init-functions


echo "myDevices agent cron job" > /var/log/cron
check_service_and_run() {
eval 'status_of_proc -p $1 /usr/bin/$2 $2'
ret_code=$?
if [ $ret_code != 0 ]; then
    echo "Restarting service $2" >> /var/log/cron
    sudo service $2 restart >> /var/log/cron
fi
}

check_service_and_run /var/run/myDevices/cayenne.pid myDevices

#rm /var/log/cron.log
rm -rf /var/log/SystemInformation.log
rm -rf /var/log/daemon*

exit

