from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class LegendarySword(Weapon):
    def __init__(self):
        super().__init__(
            name="Legendary Sword",
            description="Die Klinge der tausend Sonnen",
            price=1000,
            rarity=Rarity.LEGENDARY,
            kampftechnik=Kampftechnik.Zweihandschwerter,
            tp=Dice(12) + Dice(6),
            at_bonus=5,
            pa_bonus=3
        )
