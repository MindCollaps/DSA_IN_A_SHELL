from game.Character import Character
from game.Geldbeutel import Geldbeutel
from game.Inventory import Inventory
from item.weapon.Fist import Fist


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.inventory = Inventory()
        self.weapon_equipped = Fist()
        self.geldbeutel: Geldbeutel = Geldbeutel()

    def equip_weapon(self, weapon):
        self.weapon_equipped = weapon