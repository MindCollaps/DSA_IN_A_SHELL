from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice



class BasicBow(Weapon):
    def __init__(self):
        super().__init__("Basic Bow", "Well its a basic bow, what did you think?", 35, Rarity.COMMON,
                         Kampftechnik.Boegen, Dice(6) + 2)