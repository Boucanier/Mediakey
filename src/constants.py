"""
    This file declares constants and functions used in this project depending on the platform used.
"""
import sys
import subprocess
import os
import platform
from pynput import keyboard


if platform.system() == "Windows":

    def exec_cmd(cmd):
        """
            Execute command

            :param cmd: command to execute
            :type cmd: str
        """
        subprocess.run(cmd, shell=True, check=True)

    CMD_NEXT = "nircmd sendkey 0xB0 press"
    CMD_PREV = "nircmd sendkey 0xB1 press"
    CMD_PLAY = "nircmd sendkey 0xB3 press"

    KEYS_TRANSLATION = {
        "right": keyboard.Key.right,
        "left": keyboard.Key.left,
        "down": keyboard.Key.down,
        "up": keyboard.Key.up,
        "space": keyboard.Key.space,
        "enter": keyboard.Key.enter,
        "tab": keyboard.Key.tab,
        "esc": keyboard.Key.esc,
        "delete": keyboard.Key.delete,
        "backspace": keyboard.Key.backspace,
        "cmd": keyboard.Key.cmd,
        "ctrl": keyboard.Key.ctrl,
        "ctrl_l": keyboard.Key.ctrl_l,
        "ctrl_r": keyboard.Key.ctrl_r,
        "alt": keyboard.Key.alt,
        "shift": keyboard.Key.shift,
        "a" : keyboard.KeyCode.from_char('\x01'),
        "b" : keyboard.KeyCode.from_char('\x02'),
        "c" : keyboard.KeyCode.from_char('\x03'),
        "d" : keyboard.KeyCode.from_char('\x04'),
        "e" : keyboard.KeyCode.from_char('\x05'),
        "f" : keyboard.KeyCode.from_char('\x06'),
        "g" : keyboard.KeyCode.from_char('\x07'),
        "h" : keyboard.KeyCode.from_char('\x08'),
        "i" : keyboard.KeyCode.from_char('\x09'),
        "j" : keyboard.KeyCode.from_char('\x0a'),
        "k" : keyboard.KeyCode.from_char('\x0b'),
        "l" : keyboard.KeyCode.from_char('\x0c'),
        "m" : keyboard.KeyCode.from_char('\x0d'),
        "n" : keyboard.KeyCode.from_char('\x0e'),
        "o" : keyboard.KeyCode.from_char('\x0f'),
        "p" : keyboard.KeyCode.from_char('\x10'),
        "q" : keyboard.KeyCode.from_char('\x11'),
        "r" : keyboard.KeyCode.from_char('\x12'),
        "s" : keyboard.KeyCode.from_char('\x13'),
        "t" : keyboard.KeyCode.from_char('\x14'),
        "u" : keyboard.KeyCode.from_char('\x15'),
        "v" : keyboard.KeyCode.from_char('\x16'),
        "w" : keyboard.KeyCode.from_char('\x17'),
        "x" : keyboard.KeyCode.from_char('\x18'),
        "y" : keyboard.KeyCode.from_char('\x19'),
        "z" : keyboard.KeyCode.from_char('\x1a')
    }

elif platform.system() == "Linux":
    CMD_NEXT = "playerctl next"
    CMD_PREV = "playerctl previous"
    CMD_PLAY = "playerctl play-pause"

    SUDO_USER = os.getenv("SUDO_USER") or os.getenv("USER") or os.getenv("LOGNAME")

    def exec_cmd(cmd):
        """
            Execute command as sudo user

            :param cmd: command to execute
            :type cmd: str
        """
        subprocess.run(["su", "-", SUDO_USER, "-c", cmd], check=True)

    KEYS_TRANSLATION = {
        "right": "right",
        "left": "left",
        "down": "down",
        "up": "up",
        "space": "space",
        "enter": "enter",
        "tab": "tab",
        "esc": "esc",
        "suppr": "delete",
        "backspace": "backspace",
        "cmd": 125,
        "ctrl": "ctrl",
        "ctrl_l": "ctrl",
        "ctrl_r": "ctrl",
        "alt": "alt",
        "shift": "shift"
    }

    for ltr in "abcdefghijklmnopqrstuvwxyz":
        KEYS_TRANSLATION[ltr] = ltr

else :
    sys.exit(1)

DEFAULT_KEYS = {
    "next_key": KEYS_TRANSLATION["right"],
    "prev_key": KEYS_TRANSLATION["left"],
    "play_key": KEYS_TRANSLATION["down"],
}

CONFIG_FILE = "config/config.json"
