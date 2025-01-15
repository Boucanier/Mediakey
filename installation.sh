#! /bin/sh

# Check if the script is run as root
if [[ $EUID != 0 ]]
then
	echo This script must be run as root
	exit 1
fi


# Install the necessary packages
echo Installing packages...
sudo apt install -y python3
sudo apt install -y playerctl


#  Install the virtual environment
echo Creating virtual environment...
python3 -m venv .venv

echo Installing requirements...
./.venv/bin/pip install -r requirements_lnx.txt


# Enable sudo without password
echo Enabling execution rights...
echo "$SUDO_USER ALL=(ALL) NOPASSWD: $(pwd)/.venv/bin/python3 $(pwd)/src/mediakey.py --service" > mediakey.sudo

echo Moving mediakey.sudo...
sudo mv mediakey.sudo /etc/sudoers.d/mediakey


# Create service
echo Creating service...
echo "[Unit]
Description=Mediakey
After=network.target

[Service]
ExecStart=sudo $(pwd)/.venv/bin/python3 $(pwd)/src/mediakey.py --service
Restart=always
User=$SUDO_USER
Group=$SUDO_USER

[Install]
WantedBy=multi-user.target" > mediakey.service

echo Moving mediakey.service...
sudo mv mediakey.service /etc/systemd/system/mediakey.service

echo Reloading systemctl...
sudo systemctl daemon-reload

echo Enabling and starting service...
sudo systemctl enable mediakey.service
sudo systemctl start mediakey.service

echo -e \\nInstallation complete !
