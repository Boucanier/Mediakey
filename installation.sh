#! /bin/sh

# Check if the script is run as root
if [[ $EUID != 0 ]]
then
	echo This script must be run as root
	exit 1
fi

# Install the necessary packages
sudo apt install -y python3

#  Install the virtual environment
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt

# Enable sudo without password
echo "$SUDO_USER ALL=(ALL) NOPASSWD: $(pwd)/.venv/bin/python3 $(pwd)/src/mediakey.py --ok" > mediakey.sudo
sudo mv mediakey.sudo /etc/sudoers.d/mediakey

# Create service
echo "
Description=Mediakey
After=network.target

[Service]
ExecStart=sudo $(pwd)/.venv/bin/python3 $(pwd)/src/mediakey.py --ok
Restart=always
User=$SUDO_USER
Group=$SUDO_USER

[Install]
WantedBy=multi-user.target" > mediakey.service

sudo mv mediakey.service /etc/systemd/system/mediakey.service

sudo systemctl daemon-reload

sudo systemctl enable mediakey.service
sudo systemctl start mediakey.service
