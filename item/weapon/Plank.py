from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class Plank(Weapon):
    def __init__(self):
        super().__init__("Plank", "A peace of wood", 100, Rarity.COMMON, Kampftechnik.RAUFEN, 1 * Dice(6))
