#! /bin/sh

mediakey_count="$(ps aux | grep mediakey.py | wc -l)"

if [[ $mediakey_count -eq 1 ]]
then
    echo "Mediakey is not running"
    exit 1
else
    kill -9 $(ps aux | grep mediakey.py | head -1 | awk '{print $2}')
    echo "Mediakey stopped"
    exit 0
fi
