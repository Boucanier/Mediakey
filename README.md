# Mediakey

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

This project handle keyboard shortcuts for multimedia control (play/pause, previous track, next track)

## Requirements

At the rrot of the project you need to have a *config* folder containing a *config.json* file like this :

```json
{
    "log_path": "path/to/your/log/folder",
    "next_key": "right",
    "prev_key": "left",
    "play_key": "down"
}
```

## Installation

To simply run the program, execute the script [launch.bat](launch.bat) from the project root.

If you want the program to run at startup, execute the script [installation.bat](installation.bat) from the root project.
This will create a launcher file in your startup folder and it will start the program.

## NOTE

The program is only available for **Windows systems** now. It will soon be available for popular **Linux** distributions.
