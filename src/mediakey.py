"""
    Main file to listen to keyboard
"""
import sys
import signal
import keyboard as kb
from key_control import KeyControl
from shared import stop_event


if (sys.version_info.major, sys.version_info.minor) < (3, 10):
    print(f"You are using Python {sys.version_info.major}.{sys.version_info.minor}")
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
        key_listener.logger.error("You are using Python %s.%s, minimal version required is 3.10",
                                  sys.version_info.major,
                                  sys.version_info.minor)
        sys.exit(1)

    try:
        kb.hook(key_listener.on_hook)
        kb.wait()
    except KeyboardInterrupt:
        print("Stopping key listener...")
    finally:
        print("Key listener stopped.")


if __name__ == '__main__':
    # Attach signal handler for Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)

    # Run main function
    try:
        main()
    finally:
        # Ensure the stop_event is set and join the icon thread
        stop_event.set()
        print("Script ended properly.")
