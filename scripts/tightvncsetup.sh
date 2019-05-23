#!/bin/bash
# TightVNC setup script

which startx > /dev/null
if [ $? -eq 1 ]; then
	#startx is not installed so we just exit since VNC has X server dependencies that we don't want to install
	echo "startx is not installed"
	exit 1
fi

REALVNC_INSTALLED=$(dpkg-query -W --showformat='${Status}\n' realvnc-vnc-server | grep "install ok installed")
if [ "" != "$REALVNC_INSTALLED" ]; then
	#RealVNC is already installed so we just exit
	echo "RealVNC detected"
	exit 1
fi

# Check tightvncserver is installed
TIGHTVNC_INSTALLED=$(dpkg-query -W --showformat='${Status}\n' tightvncserver | grep "install ok installed")
if [ "" == "$TIGHTVNC_INSTALLED" ]; then
	sudo apt-get --yes install tightvncserver
	touch "${uninstallpath}/installed_package"
	echo tightvncserver >> "${uninstallpath}/installed_package"
fi

which tightvncserver > /dev/null

if [ $? -eq 1 ]; then
	#TightVNC is not installed so we just exit
	echo "TightVNC not installed"
	exit 1
fi

declare -a dependencies=("xfonts-base" "expect")
for dependency in "${dependencies[@]}"
do
	PACKAGE_INSTALLED=$(dpkg-query -W --showformat='${Status}\n' $dependency | grep "install ok installed")
	if [ "" == "$PACKAGE_INSTALLED" ]; then
		sudo apt-get --yes install $dependency
		touch "${uninstallpath}/installed_package"
		echo "$dependency" >> "${uninstallpath}/installed_package"
	fi
done

if [ -f ~cayenne/.vnc/passwd ]; then
	echo "VNC password file already exists"
	exit 1
fi

#if it`s first time the passwd setup must be done
prog=/usr/bin/vncpasswd
mypass="myDevices"
sudo -u cayenne /usr/bin/expect <<EOF
log_user 0
spawn "$prog"
expect "Password:"
send "$mypass\r"
expect "Verify:"
send "$mypass\r"
expect "Would you like to enter a view-only password"
send "n\r"
expect eof
exit
EOF
if [ $? -eq 1 ]; then
	echo "Error setting VNC password"
else
	echo "VNC password set"
fi