from game import Player
from item import Rarity
from item import Weapon
from npc import Enemy


class LegendarySword(Weapon):
    def __init__(self):
        super().__init__("The Master Sword", 40, Rarity.LEGENDARY, 18, 0.3, 4, 25)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()
