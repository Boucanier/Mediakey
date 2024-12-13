"""
    Main file to listen to keyboard
"""
import sys
from key_control import key_control, keyboard


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["--ok", "--force"]:
        sys.exit(1)

    key_listener = key_control()

    with keyboard.Listener(
            on_press=key_listener.on_press,
            on_release=key_listener.on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()
