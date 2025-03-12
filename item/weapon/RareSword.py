from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class RareSword(Weapon):
    def __init__(self):
        super().__init__(
            name="Runenschwert",
            description="Schwert mit glühenden Runen",
            price=200,
            rarity=Rarity.RARE,
            kampftechnik=Kampftechnik.Schwerter,
            tp=Dice(8) + 1,
            pa_bonus=2
        )
