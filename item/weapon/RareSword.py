from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice



class RareSword(Weapon):
    def __init__(self):
        super().__init__("Rare Sword", "The Kusanagi Sword is a legendary Japanese blade with mythical powers to control the wind.",
                        10, Rarity.COMMON, Kampftechnik.Schwerter, Dice(6) + 3)