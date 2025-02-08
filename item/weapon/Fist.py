from game import Player
from item import Rarity
from item import Weapon
from npc import Enemy


class Fist(Weapon):
    def __init__(self):
        super().__init__("Fist", 0, Rarity.COMMON, 2, 0.0, 0, 100)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()
