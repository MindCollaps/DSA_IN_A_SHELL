from item import Item

class Inventory:
    def __init__(self):
        self.inventory: list[Item] = []

    def inventory_dialog_normal(self):
        print("Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i + 1}. {item.name}")
        print()

    def inventory_dialog_fight(self):
        print("Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i + 1}. {item.name}")
        print()
