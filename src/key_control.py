"""
    Class to handle key press and release events
"""
import os
import subprocess
import json
from datetime import datetime
import logging
from pynput import keyboard

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
}

DEFAULT_KEYS = {
    "next_key": KEYS_TRANSLATION["right"],
    "prev_key": KEYS_TRANSLATION["left"],
    "play_key": KEYS_TRANSLATION["down"],
}

class key_control:
    """
        Class to handle key press and release events
    """
    def __init__(self):
        self.ctrl_key = False
        self.win_key = False
        self.logger = self.create_logger()
        self.next_key, self.prev_key, self.play_key = self.assign_keys()


    def create_logger(self):
        """
            Create logger

            :return: logger
            :rtype: logging.Logger
        """
        today = datetime.now().strftime("%Y-%m-%d")
        with open("config/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            log_path = config["log_path"]

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        logger = logging.getLogger(today)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler(os.path.join(log_path, f"{today}.log"))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.info('Logger created successfully')
        return logger


    def assign_keys(self):
        """
            Assign keys from config file

            :return: next_key, prev_key, play_key
            :rtype: tuple
        """
        next_key = DEFAULT_KEYS["next_key"]
        prev_key = DEFAULT_KEYS["prev_key"]
        play_key = DEFAULT_KEYS["play_key"]

        try :
            with open("config/config.json", "r", encoding="utf-8") as f:
                self.logger.info("Reading config file")
                config = json.load(f)
                next_key = KEYS_TRANSLATION[config["next_key"]]
                prev_key = KEYS_TRANSLATION[config["prev_key"]]
                play_key = KEYS_TRANSLATION[config["play_key"]]

            self.logger.info("Keys assigned successfully")

        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            self.logger.error("Error: %s", e)
            self.logger.info("Using default keys")

        return next_key, prev_key, play_key


    def on_press(self, key):
        """
            Detect key press event and check if ctrl or cmd key is pressed

            :param key: key pressed
            :type key: pynput.keyboard.Key
        """
        # Check if Ctrl key is pressed
        if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            self.ctrl_key = True
        if key == keyboard.Key.cmd:
            self.win_key = True


    def on_release(self, key):
        """
            Detect key release event and execute command if key combination is detected

            :param key: key released
            :type key: pynput.keyboard.Key

            :return: False if error occurs (subprocess.CalledProcessError), True otherwise
            :rtype: bool
        """
        # Detect Ctrl + X combination
        try :
            if key == self.next_key and self.ctrl_key and self.win_key :
                subprocess.run("nircmd sendkey 0xB0 press", shell=True, check=True)
                self.logger.info("Next key pressed")

            elif key == self.prev_key and self.ctrl_key and self.win_key :
                subprocess.run("nircmd sendkey 0xB1 press", shell=True, check=True)
                self.logger.info("Previous key pressed")

            elif key == self.play_key and self.ctrl_key and self.win_key :
                subprocess.run("nircmd sendkey 0xB3 press", shell=True, check=True)
                self.logger.info("Play key pressed")

            if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
                self.ctrl_key = False

            elif key == keyboard.Key.cmd:
                self.win_key = False

        except subprocess.CalledProcessError as e:
            self.logger.error("Error: %s", e)
            return False

        return True
