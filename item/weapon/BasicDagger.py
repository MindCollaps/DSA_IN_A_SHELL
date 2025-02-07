from game import Player
from item import Weapon
from item import Rarity
from npc import Enemy

import random


class BasicDagger(Weapon):
    def __init__(self):
        super().__init__("Basic Dagger", 8, Rarity.COMMON, 6, 0.1, 3, 100)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()