from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class Fist(Weapon):
    def __init__(self):
        super().__init__("Fist", "Well its your fist", 0, Rarity.COMMON, Kampftechnik.RAUFEN, 1*Dice(6))
