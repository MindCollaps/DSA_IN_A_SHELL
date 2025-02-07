from game import Player
from item import Weapon
from item import Rarity
from npc import Enemy

import random


class RareSword(Weapon):
    def __init__(self):
        super().__init__("Kusanagi Sword", 17, Rarity.RARE, 14, 0.2, 2, 75)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()