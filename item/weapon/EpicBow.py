from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice



class EpicBow(Weapon):
    def __init__(self):
        super().__init__("Epic Bow", "Its called Shadow String", 220, Rarity.EPIC,
                         Kampftechnik.Boegen, Dice(6) + 5)