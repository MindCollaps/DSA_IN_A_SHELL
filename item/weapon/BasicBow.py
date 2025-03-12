from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class BasicBow(Weapon):
    def __init__(self):
        super().__init__(
            name="Basic Bow",
            description="Ein einfacher Bogen für Anfänger",
            price=35,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.Boegen,
            tp=Dice(6) + 2,
            at_bonus=1
        )
