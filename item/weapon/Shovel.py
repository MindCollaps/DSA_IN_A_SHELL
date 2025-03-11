from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class Shovel(Weapon):
    def __init__(self):
        super().__init__(
            name="Rusty Shovel",
            description="Landwirtschaftliches Werkzeug",
            price=5,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.Stangenwaffen,
            tp=1 * Dice(6),
            pa_bonus=-1
        )