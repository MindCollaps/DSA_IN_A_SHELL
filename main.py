from rich.color import Color

from utils import MenuOption
from utils import Printer

if __name__ == "__main__":
    console = Printer()
    options = [MenuOption("Test 1", color=Color.from_rgb(0, 0, 255)),
               MenuOption("Test 2", sub_menu=[MenuOption("Sub 1"), MenuOption("Sub 2")])]
    first, second = console.menu(options)
