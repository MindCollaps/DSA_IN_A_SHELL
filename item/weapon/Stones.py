from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class Stones(Weapon):
    def __init__(self):
        super().__init__("Bunch of Stones", "Well its a bunch of Stones, atleast you can keep distance", 0, Rarity.COMMON, Kampftechnik.Wurfwaffen, 1 * Dice(6))
