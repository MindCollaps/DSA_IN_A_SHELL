from game.Kampftechnik import Kampftechnik
from item import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class EpicKatana(Weapon):
    def __init__(self):
        super().__init__("Epic Katana", "Yorukaze (night wind) is a epic Katana", 320, Rarity.EPIC,
                         Kampftechnik.Zweihandschwerter, Dice(6) + 5)