from item import Item
from utils import Printer


class Inventory:
    def __init__(self):
        self.inventory: list[Item] = []

    def inventory_dialog_normal(self, console: Printer):
        console.println("Inventory")

    def inventory_dialog_fight(self, console: Printer):
        print("Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i + 1}. {item.name}")
        print()
