from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class Warhammer(Weapon):
    def __init__(self):
        super().__init__("Warhammer", "A heavy powerful weapon from old forgotten wars", 0, Rarity.EPIC, Kampftechnik.Zweihandhiebwaffen, Dice(6) + 5 )
