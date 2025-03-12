from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class Plank(Weapon):
    def __init__(self):
        super().__init__(
            name="Rotted Plank",
            description="Ein morsches Brett mit Nagel",
            price=2,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.Hiebwaffen,
            tp=1 * Dice(4),
            at_bonus=-1
        )
