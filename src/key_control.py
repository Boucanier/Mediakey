"""
    Class to handle key press and release events
"""
import os
from subprocess import CalledProcessError
import json
from datetime import datetime
import logging
from constants import CONFIG_FILE, DEFAULT_KEYS, KEYS_TRANSLATION, CMD_NEXT, CMD_PREV, CMD_PLAY, exec_cmd


class KeyControl:
    """
        Class to handle key press and release events
    """
    def __init__(self):
        self.ctrl_key = False
        self.win_key = False
        self.logger = self.create_logger()
        self.next_key, self.prev_key, self.play_key = self.assign_keys()


    def create_logger(self) -> logging.Logger :
        """
            Create logger

            :return: logger
            :rtype: logging.Logger
        """
        today = datetime.now().strftime("%Y-%m-%d")
        try :
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
                log_path = config["log_path"]

        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            log_path = "logs"

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


    def assign_keys(self) -> tuple :
        """
            Assign keys from config file

            :return: next_key, prev_key, play_key
            :rtype: tuple
        """
        next_key = DEFAULT_KEYS["next_key"]
        prev_key = DEFAULT_KEYS["prev_key"]
        play_key = DEFAULT_KEYS["play_key"]

        try :
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
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


    def on_hook(self, event) -> None:
        if event.event_type == "down":
            self.on_press(event.scan_code)
        elif event.event_type == "up":
            self.on_release(event.scan_code)


    def on_press(self, key) -> None :
        """
            Detect key press event and check if ctrl or cmd key is pressed

            :param key: key pressed
            :type key: pynput.keyboard.Key
        """
        # Check if Ctrl key is pressed
        if key in (KEYS_TRANSLATION["ctrl_l"], KEYS_TRANSLATION["ctrl_r"]):
            self.ctrl_key = True
        if key == KEYS_TRANSLATION["cmd"]:
            self.win_key = True


    def on_release(self, key) -> bool:
        """
            Detect key release event and execute command if key combination is detected

            :param key: key released
            :type key: pynput.keyboard.Key

            :return: False if error occurs (subprocess.CalledProcessError), True otherwise
            :rtype: bool
        """
        # Detect Ctrl + X combination
        if key == self.play_key and self.ctrl_key and self.win_key :
            self.logger.info("Play key pressed")
        elif key == self.next_key and self.ctrl_key and self.win_key :
            self.logger.info("Next key pressed")
        elif key == self.prev_key and self.ctrl_key and self.win_key :
            self.logger.info("Previous key pressed")

        try :
            if key == self.play_key and self.ctrl_key and self.win_key :
                exec_cmd(CMD_PLAY)

            elif key == self.next_key and self.ctrl_key and self.win_key :
                exec_cmd(CMD_NEXT)

            elif key == self.prev_key and self.ctrl_key and self.win_key :
                exec_cmd(CMD_PREV)

            if key in (KEYS_TRANSLATION["ctrl_l"], KEYS_TRANSLATION["ctrl_r"]):
                self.ctrl_key = False

            elif key == KEYS_TRANSLATION["cmd"]:
                self.win_key = False

        except CalledProcessError as e:
            self.logger.error("%s", e)
            return False

        return True
