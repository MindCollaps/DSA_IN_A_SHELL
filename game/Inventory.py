from rich.color import Color
from rich.style import Style

from item import Item
from item.usable.Usable import Usable
from item.weapon.Weapon import Weapon
from utils.ConsolePrinter import Printer, MenuOption


class Inventory:
    def __init__(self):
        self.inventory: list[Item] = []

    def add_item(self, item: Item):
        self.inventory.append(item)

    def inventory_dialog(self, printer: Printer, player, fight: bool = False) -> (bool, bool):
        printer.clear()
        printer.println("")
        options = []

        for i, item in enumerate(self.inventory):
            subMenu = []

            des = MenuOption("Description")
            # IDE says this is wrong, but it works, trust me
            des.selected = lambda item=item: printer.println(
                f"Description:\n{item.get_description(player)}" if isinstance(item,
                                                                              Weapon) else f"Description:\n{item.description}")
            subMenu.append(des)

            if isinstance(item, Usable):
                op = MenuOption("Use")
                op.selected = lambda item=item: player.consume(item, printer)
                subMenu.append(op)

            isEquiped = False
            if isinstance(item, Weapon):
                if item is player.weapon_equipped:
                    isEquiped = True
                    op = MenuOption("Unequip")
                    op.selected = lambda item=item: {
                        player.equip_weapon(None),
                        printer.println(f"You unequip {item.name}")
                    }
                    subMenu.append(op)
                else:
                    op = MenuOption("Equip")
                    op.selected = lambda item=item: {
                        player.equip_weapon(item),
                        printer.println(f"You equip {item.name}")
                    }
                    subMenu.append(op)

            options.append(MenuOption(item.name if not isEquiped else item.name + " (Equipped)", sub_menu=subMenu))

        options.append(MenuOption("Close"))

        choice, second_choice = printer.menu(options, title="Inventory",
                                             border_style=Style(color=Color.from_rgb(100, 0, 255)))
        printer.clear()

        if second_choice != -1:
            option = options[choice].sub_menu[second_choice]
            if hasattr(option, 'selected') and callable(option.selected):
                option.selected()
                printer.wait(wait_message=True)
                if second_choice == 0:
                    return False, False
                else:
                    return True, False
        else:
            option = options[choice]
            if hasattr(option, 'selected') and callable(option.selected):
                option.selected()
                printer.wait(wait_message=True)
                if second_choice == 0:
                    return False, False
                else:
                    return True, False

        if choice == len(options) - 1:
            return False, True

        return False, False

    def remove_item(self, item_to_remove):
        # Entfernt das erste gefundene Item
        for idx, item in enumerate(self.inventory):
            if item is item_to_remove:
                del self.inventory[idx]
                break
