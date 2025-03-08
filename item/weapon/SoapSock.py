from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class SoapSock(Weapon):
    def __init__(self):
        super().__init__("Soap Sock", "Its a soap in a sock, so what?", 25, Rarity.COMMON, Kampftechnik.Hiebwaffen, Dice(6) + 1)