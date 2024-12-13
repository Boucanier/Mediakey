"""
    Class to handle key press and release events
"""
import os
import subprocess
import json
from datetime import datetime
import logging
from pynput import keyboard

class key_control:
    def __init__(self):
        self.ctrl_key = False
        self.win_key = False
        self.logger = self.create_logger()
        self.next_key = keyboard.Key.right
        self.prev_key = keyboard.Key.left
        self.play_key = keyboard.Key.down


    def create_logger(self):
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


    def on_press(self, key):
        # Check if Ctrl key is pressed
        if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            self.ctrl_key = True
        if key == keyboard.Key.cmd:
            self.win_key = True


    def on_release(self, key):
        # Detect Ctrl + X combination
        try :
            if key == self.next_key and self.ctrl_key and self.win_key :
                subprocess.run("nircmd sendkey 0xB0 press", shell=True, check=True)

            elif key == self.prev_key and self.ctrl_key and self.win_key :
                subprocess.run("nircmd sendkey 0xB1 press", shell=True, check=True)

            elif key == self.play_key and self.ctrl_key and self.win_key :
                subprocess.run("nircmd sendkey 0xB3 press", shell=True, check=True)

            if key in (keyboard.Key.alt_l, keyboard.Key.alt_r):
                self.ctrl_key = False

            elif key == keyboard.Key.cmd:
                self.win_key = False

        except subprocess.CalledProcessError as e:
            self.logger.error("Error: %s", e)
            return False

        return True
