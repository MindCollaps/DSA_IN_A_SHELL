from game import Player
from item import Weapon
from item import Rarity
from npc import Enemy

import random


class EpicBow(Weapon):
    def __init__(self):
        super().__init__("Shadow String, Bow", 20, Rarity.EPIC, 18, 0.3, 3, 45)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()