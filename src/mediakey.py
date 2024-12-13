"""
    Main file to listen to keyboard
"""
from key_control import key_control, keyboard

def main():
    key_listener = key_control()

    with keyboard.Listener(
            on_press=key_listener.on_press,
            on_release=key_listener.on_release) as listener:
        listener.join()

if __name__ == '__main__':
    main()
