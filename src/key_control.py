"""
    Class to handle key press and release events
"""
import subprocess
from pynput import keyboard

class key_control:
    def __init__(self):
        self.ctrl_key = False

    def on_press(self, key):
        # Check if Ctrl key is pressed
        if key in (keyboard.Key.alt_l, keyboard.Key.alt_r):
            self.ctrl_key = True

    def on_release(self, key):
        # Detect Ctrl + X combination
        if key == keyboard.Key.right and self.ctrl_key :
            subprocess.run("nircmd sendkey 0xB0 press", shell=True, check=True)

        self.ctrl_key = False

        # Stop listener on Esc key
        if key == keyboard.Key.esc:
            return False

        return True
