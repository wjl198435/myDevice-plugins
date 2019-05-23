#!/bin/bash
# myDevices uninstall script
set -e
PROJECT_PATH=/etc/myDevices
uninstallpath=${PROJECT_PATH}/uninstall
WEBIOPI_PATH=/etc/webiopi
WEBIOPI_UNINSTALL_PATH=${WEBIOPI_PATH}/uninstall
args=("$@")
ELEMENTS=${#args[@]}
FULL_REMOVE=0

service cron stop
service myDevices stop

for (( i=0;i<$ELEMENTS;i++)); do
    if [ "${args[${i}]}" == "-full" ]; then
		FULL_REMOVE=1
    fi
done;

#agent python code removed
#cat "${uninstallpath}/installed_agent" | xargs rm -rf
sed -n 's/\(myDevices.*egg\).*/\1/p' /etc/myDevices/uninstall/installed_agent | sort -u | xargs rm -rf

#if full flag is present also installed dependencies are removed
if [ $FULL_REMOVE == 1 ]; then
	cat ${uninstallpath}/installed_components_* | xargs rm -rf

	if [ -f "${uninstallpath}/installed_deb" ]; then
		cat ${uninstallpath}/installed_deb | xargs sudo dpkg -r
	fi

	#if we haven't previously uninstalled webiopi, remove it now
	if [ ! -f "${uninstallpath}/webiopi_uninstalled" ] && [ -f "${WEBIOPI_UNINSTALL_PATH}/uninstall.sh" ]; then

		bash "${WEBIOPI_UNINSTALL_PATH}/uninstall.sh"
	fi
fi

#remove binary
rm -rf /usr/bin/myDevices

#remove services
if pgrep "systemd" > /dev/null; then
	# Remove systemd service
	systemctl disable myDevices
	rm -rf /etc/systemd/system/myDevices.service
else
	# Remove init.d service/daemon script
	rm -rf /etc/init.d/myDevices
fi
systemctl daemon-reload

rm -rf /var/log/myDevices*
rm -rf /var/run/myDevices

#remove folder path
rm -rf "${PROJECT_PATH}"

sed -i '/.*myDevices.*/d' /var/spool/cron/crontabs/root

#remove cayenne user
set +e # Don't exit if these fail. The killall command will fail if no cayenne processes are running.
killall -u cayenne
userdel -r cayenne
groupdel cayenne

service cron start