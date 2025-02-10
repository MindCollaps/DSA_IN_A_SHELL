from game.Inventory import Inventory
from game.Character import Character
from item.weapon.Fist import Fist


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.inventory = Inventory()
        self.weapon_equipped = Fist()
