from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice




class LegendarySword(Weapon):
    def __init__(self):
        super().__init__("The Master Sword", "Its a legendary blade, forged by divine power, known as the sword that seals the darkness", 
                         500, Rarity.LEGENDARY, Kampftechnik.Schwerter, Dice(6) + 6)