#! /bin/sh

# Check if the script is run as root
if [[ $EUID != 0 ]]
then
	echo This script must be run as root
	exit 1
fi

read -p "Are you sure you want to uninstall Mediakey? (y/n) : " answer
if [[ $answer != "y" ]]
then
    echo Uninstallation cancelled.
    exit 0
fi

# Stop the service if it is running
if systemctl is-active --quiet mediakey.service
then
	echo Stopping mediakey service...
	sudo systemctl stop mediakey.service
fi

echo Removing mediakey.sudo...
if [ -f /etc/sudoers.d/mediakey ];
then
    sudo rm /etc/sudoers.d/mediakey
else
    echo "mediakey.sudo not found in /etc/sudoers.d/"
fi

echo Removing mediakey.service...
if [ -f /etc/systemd/system/mediakey.service ];
then
    sudo rm /etc/systemd/system/mediakey.service
else
    echo "mediakey.service not found in /etc/systemd/system/"
fi

echo Reloading systemctl...
sudo systemctl daemon-reload

echo Removing virtual environment...
if [ -d .venv ];
then
    rm -rf .venv
else
    echo "Virtual environment '.venv' not found."
fi

echo -e \\nUninstalled Mediakey successfully.
