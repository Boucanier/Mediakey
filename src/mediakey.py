"""
    Main file to listen to keyboard
"""
import sys
import signal
import threading
from key_control import KeyControl, keyboard
from icon import run_icon
from shared import stop_event


if (sys.version_info.major, sys.version_info.minor) < (3, 10):
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))
    print("This script requires Python 3.10 or higher")
    print("\nYou can download it from https://www.python.org/downloads/")
    sys.exit(1)


def handle_interrupt(signal, frame) -> None :
    """
        Handle Ctrl+C to stop the script cleanly.

        :param signal: signal number
        :type signal: int
        :param frame: current stack frame
        :type frame: frame object
    """
    print("\nDetected Ctrl+C. Stopping the script...")
    stop_event.set()


def main():
    """
        Main function to listen to keyboard and execute commands

        :param sys.argv: command line arguments
        :type sys.argv: list
        
    """
    if len(sys.argv) != 2 or sys.argv[1] not in ["--ok", "--force"]:
        print("Usage: python main.py [--ok | --force]")
        sys.exit(1)

    key_listener = KeyControl()
    
    if (sys.version_info.major, sys.version_info.minor) < (3, 10):
        key_listener.logger.error("You are using Python {}.{}, minimal version required is 3.10".format(sys.version_info.major, sys.version_info.minor))
        sys.exit(1)

    try:
        with keyboard.Listener(
                on_press=key_listener.on_press,
                on_release=key_listener.on_release) as listener:
            while not stop_event.is_set():
                listener.join(1)  # Check stop event every second
    except KeyboardInterrupt:
        print("Stopping key listener...")
    finally:
        print("Key listener stopped.")


if __name__ == '__main__':
    # Attach signal handler for Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)

    # Start icon in a new thread
    icon_thread = threading.Thread(target=run_icon, daemon=True)
    icon_thread.start()

    # Run main function
    try:
        main()
    finally:
        # Ensure the stop_event is set and join the icon thread
        stop_event.set()
        icon_thread.join()
        print("Script ended properly.")
