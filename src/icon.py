"""
    File to create the icon in the system tray.
"""
import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
from shared import stop_event


# Create icon image
def create_image() -> Image.Image :
    """
        Create icon image

        :return: Image
        :rtype: PIL.Image.Image
    """
    width = 64
    height = 64
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.polygon([(0,0), (0, height), (width, height//2)], fill = (100,125,235))
    return image


# Function to quit cleanly
def quit_program(tray_icon : Icon) -> None :
    """
        Quit the program

        :param icon: Icon
        :type icon: pystray.Icon
    """
    stop_event.set()  # Signal main thread to stop
    tray_icon.stop()       # Stop the icon


# Create context menu
menu = Menu(
    MenuItem('★ MEDIAKEY ★', None, enabled=False),
    Menu.SEPARATOR,
    MenuItem('Quit', quit_program)
)

# Create and configure the icon
icon = Icon(
    "TempIcon",
    create_image(),
    menu=menu,
    title="Mediakey"
)


# Start icon in a new thread
def run_icon() -> None :
    """
        Run the icon, checking periodically for the stop_event.
    """
    def check_stop():
        while not stop_event.is_set():
            icon.visible = True
            stop_event.wait(0.5)  # Check every 500 ms
        icon.stop()

    icon_thread = threading.Thread(target=check_stop, daemon=True)
    icon_thread.start()
    icon.run()
