from game import Player
from item import Weapon
from item import Rarity
from npc import Enemy

import random


class RareWand(Weapon):
    def __init__(self):
        super().__init__("Non-magical wand", 12, Rarity.RARE, 12, 0.1, 2, 75)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()