from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class BasicDagger(Weapon):
    def __init__(self):
        super().__init__(
            name="Basic Dagger",
            description="Ein einfacher Dolch mit scharfer Klinge",
            price=15,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.Dolche,
            tp=Dice(4) + 1,
            at_bonus=2
        )