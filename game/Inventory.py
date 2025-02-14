from rich.layout import Layout

from item import Item
from utils import Printer


class Inventory:
    def __init__(self):
        self.inventory: list[Item] = []

    def inventory_dialog_normal(self, console: Printer, fight: bool = False):
        layout = Layout()
        layout.split_column(
            Layout(name="menu", )
        )

    def inventory_dialog_fight(self, console: Printer):
        self.inventory_dialog_normal(console, fight=True)
