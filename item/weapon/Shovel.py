from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class Fist(Weapon):
    def __init__(self):
        super().__init__("Shovel", "A rusty shovel, maybe you can bonk someones head", 0, Rarity.COMMON, Kampftechnik.Zweihandhiebwaffen, Dice(6) + 1)
