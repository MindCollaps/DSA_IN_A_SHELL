from game import Player
from item import Weapon
from item import Rarity
from npc import Enemy

import random


class Plank(Weapon):
    def __init__(self):
        super().__init__("Plank", 0, Rarity.COMMON, 8, 0, 0, 20)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()