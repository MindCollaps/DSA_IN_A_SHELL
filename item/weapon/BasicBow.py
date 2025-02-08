from game import Player
from item import Rarity
from item import Weapon
from npc import Enemy


class BasicBow(Weapon):
    def __init__(self):
        super().__init__("Basic Bow", 11, Rarity.COMMON, 9, 0.2, 3, 90)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()
