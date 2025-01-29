#! /bin/sh

mediakey_count="$(ps aux | grep mediakey.py | wc -l)"

if [[ $mediakey_count -eq 1 ]]
then
    echo "Mediakey is not running"
    sudo ./.venv/bin/python3 src/mediakey.py --ok &
    echo "Mediakey started"
    exit 0
else
    echo "Mediakey is already running"
    exit 1
fi
