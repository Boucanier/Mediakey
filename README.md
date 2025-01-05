# Mediakey

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

This project handle keyboard shortcuts for multimedia control (play/pause, previous track, next track)

## Requirements

At the root of the project you need to have a *config* folder containing a *config.json* file like this :

```json
{
    "log_path": "path/to/your/log/folder",
    "next_key": "right",
    "prev_key": "left",
    "play_key": "down"
}
```

To run the program you need the following softwares :

- [Python 3.10](https://www.python.org/downloads/) or above
- [nircmd](https://www.nirsoft.net/utils/nircmd.html) (for Windows only, in your Windows directory)

## Installation and running

### Installation

If you want the program to run at startup, execute the script [installation.bat](installation.bat) from the project root.
This will create a launcher file in your startup folder and it will start the program. This will also create a virtual environment in the project root (***.venv***).

If you want to remove the program from the startup, execute the script [uninstall.bat](uninstall.bat) from the project root.

### Virtual environment

If you have installed the program with the [installation script](#installation), you don't need to create the virtual environment.

Otherwise, you have to create a Python virtual environment in the project root :

```bash
python -m venv .venv
```

Then you have to activate the virtual environment :

```bash
./.venv/Scripts/activate (Windows)
source .venv/bin/activate (Linux)
```

Then you have to install the required packages :

```bash
pip install -r requirements.txt
```

To deactivate the virtual environment :

```bash
deactivate
```

### Running

To simply run the program, execute the script [launch.bat](launch.bat) from the project root (you need to have created [the virtual env](#virtual-environment)).

To stop the program, execute the script [stop.bat](stop.bat) from the root project or right click on the Mediakey icon in your system tray and click on "**Quit**".

Once the program is running, you can control your multimedia player with the following shortcuts :

- next track : **ctrl + windows + right**
- previous track : **ctrl + windows + left**
- play/pause : **ctrl + windows + down**

The arrow keys can be changed in the *config/config.json* file.

## NOTE

The program is only available for **Windows systems** now. It will soon be available for popular **Linux** distributions.
