from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class BasicDagger(Weapon):
    def __init__(self):
        super().__init__("Basic Dagger", "Well its a basic dagger, what did you think?", 45, Rarity.COMMON,
                         Kampftechnik.Dolche, Dice(6) + 1)
