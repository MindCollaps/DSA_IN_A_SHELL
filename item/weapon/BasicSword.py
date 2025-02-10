from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class BasicSword(Weapon):
    def __init__(self):
        super().__init__("Basic Sword", "Well its a basic sword, what did you think?", 10, Rarity.COMMON, Kampftechnik.Schwerter,  Dice(6)+2)
