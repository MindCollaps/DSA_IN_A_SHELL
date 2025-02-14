from game import Player
from game.Kampftechnik import Kampftechnik
from item import Rarity
from item import Weapon
from npc import Enemy
from utils.dice.Dices import Dice


class SoapSock(Weapon):
    def __init__(self):
        super().__init__("Soap in a Sock", "Knastwaffe",2, Rarity.COMMON, Kampftechnik.RAUFEN, 1 * Dice(6))

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()
