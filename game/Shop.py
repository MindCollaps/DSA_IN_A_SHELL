from utils.ConsolePrinter import Printer, MenuOption
from game.Random import items, weapons
import random


class Shop:
    def __init__(self, player):
        self.player = player
        self.printer = Printer()
        # Item-Instanzen aus den ItemPossibility-Objekten extrahieren
        self.items = random.sample([ip.item for ip in items + weapons], 5)

    def start_shop(self):
        while True:
            self.printer.clear()
            self.printer.println("=== SHOP ===")
            # Aktuelle Kreuzer direkt aus dem Character-Objekt holen
            self.printer.println(f"Kreuzer: {self.player.geldbeutel.kreuzer}\n")

            # Menüoptionen mit tatsächlichen Item-Preisen
            options = [
                MenuOption(f"{item.name} - {item.price} Kreuzer")
                for item in self.items
            ]
            options.append(MenuOption("Verlassen"))

            choice, _ = self.printer.menu(options)

            if choice == len(options) - 1:
                break
            # Direktes Item-Objekt übergeben
            self.handle_purchase(self.items[choice])

    def handle_purchase(self, item):
        if self.player.geldbeutel.kreuzer >= item.price:
            self.player.geldbeutel.kreuzer -= item.price
            self.player.inventory.add_item(item)
            self.printer.println(f"Erfolgreich gekauft: {item.name}!")
        else:
            self.printer.println("Nicht genug Kreuzer!")
        self.printer.wait()