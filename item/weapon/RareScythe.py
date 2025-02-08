from game import Player
from item import Rarity
from item import Weapon
from npc import Enemy


class RareScythe(Weapon):
    def __init__(self):
        super().__init__("Lunar Scythe", 15, Rarity.RARE, 13, 0.2, 3, 75)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()
