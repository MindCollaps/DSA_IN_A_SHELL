from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class BasicSword(Weapon):
    def __init__(self):
        super().__init__(
            name="Basic Sword",
            description="Ein standard Einhandschwert",
            price=50,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.Schwerter,
            tp=Dice(6) + 2,
            pa_bonus=1
        )
