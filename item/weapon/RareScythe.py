from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice



class RareScythe(Weapon):
    def __init__(self):
        super().__init__("Lunar Scythe", "Its a mystical crescent blade imbued with lunar powers", 10, Rarity.RARE,
                         Kampftechnik.Zweihandschwerter, Dice(6) + 3)