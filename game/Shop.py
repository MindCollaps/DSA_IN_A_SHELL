import random

from rich.color import Color
from rich.style import Style

from game.Random import items, weapons
from item.weapon.Fist import Fist  # Für die Fist-Überprüfung
from utils.ConsolePrinter import Printer, MenuOption


class Shop:
    def __init__(self, player):
        self.player = player
        self.printer = Printer()
        self.items = random.sample([ip.item for ip in items + weapons], 5)
        self.printer.use_layout()

    def start_shop(self):
        while True:
            self.printer.clear()
            self.printer.println(f"Kreuzer: {self.player.geldbeutel.kreuzer}\n")

            # Hauptmenü mit Kaufen/Verkaufen
            main_options = [
                MenuOption("Gegenstände kaufen"),
                MenuOption("Gegenstände verkaufen"),
                MenuOption("Verlassen")
            ]

            choice, _ = self.printer.menu(main_options, title="Shop",
                                          border_style=Style(color=Color.from_rgb(252, 169, 3)))

            if choice == 0:
                self.show_buy_menu()
            elif choice == 1:
                self.show_sell_menu()
            elif choice == 2:
                break

    def show_buy_menu(self):
        while True:
            self.printer.clear()
            self.printer.println(f"Kreuzer: {self.player.geldbeutel.kreuzer}\n")

            options = [
                MenuOption(f"{item.name} - {item.price} Kreuzer")
                for item in self.items
            ]
            options.append(MenuOption("Zurück"))

            choice, _ = self.printer.menu(options)

            if choice == len(options) - 1:
                break
            self.handle_purchase(self.items[choice])

    def show_sell_menu(self):
        while True:
            self.printer.clear()
            self.printer.println(f"Kreuzer: {self.player.geldbeutel.kreuzer}\n")

            # Sellable items JEDES MAL neu ermitteln
            sellable_items = [item for item in self.player.inventory.inventory
                              if not isinstance(item, Fist)]

            if not sellable_items:
                self.printer.println("Keine verkaufbaren Gegenstände!")
                self.printer.wait()
                return

            options = [
                MenuOption(f"{item.name} - {self.calculate_sell_price(item)} Kreuzer")
                for item in sellable_items
            ]
            options.append(MenuOption("Zurück"))

            choice, _ = self.printer.menu(options)

            if choice == len(options) - 1:
                break

            # Sicherstellen dass das Item noch existiert
            sold_item = sellable_items[choice]
            if sold_item not in self.player.inventory.inventory:
                self.printer.println("Gegenstand existiert nicht mehr!")
                self.printer.wait()
                break

            self.handle_sale(sold_item)
            break  # Menü nach Verkauf neu laden

    def calculate_sell_price(self, item):
        return max(1, int(item.price * 0.5))  # 50% des Originalpreises

    def handle_purchase(self, item):
        if self.player.geldbeutel.kreuzer >= item.price:
            self.player.geldbeutel.kreuzer -= item.price
            self.player.inventory.add_item(item)
            self.printer.println(f"Gekauft: {item.name}!")
        else:
            self.printer.println("Nicht genug Kreuzer!")
        self.printer.wait()

    def handle_sale(self, item):
        sell_price = self.calculate_sell_price(item)
        self.player.geldbeutel.kreuzer += sell_price
        self.player.inventory.remove_item(item)
        self.printer.println(f"Verkauft: {item.name} für {sell_price} Kreuzer!")
        self.printer.wait()
