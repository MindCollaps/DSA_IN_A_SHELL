from game import Player
from item import Rarity
from item import Weapon
from npc import Enemy


class SoapSock(Weapon):
    def __init__(self):
        super().__init__("Soap in a Sock", 2, Rarity.COMMON, 3, 0.1, 2, 30)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()
