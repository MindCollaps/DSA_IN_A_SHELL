from game import Player
from item import Weapon
from item import Rarity
from npc import Enemy

import random


class BasicSword(Weapon):
    def __init__(self):
        super().__init__("Basic Sword", 10, Rarity.COMMON, 10, 0.1, 2, 100.0)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()