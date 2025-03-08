from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class RareWand(Weapon):
    def __init__(self):
        super().__init__("Rare Wand", "Its a non magical wand, so its just a large plank", 85, Rarity.RARE,
                                  Kampftechnik.Stangenwaffen, Dice(6) + 2)
