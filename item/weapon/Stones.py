from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class Stones(Weapon):
    def __init__(self):
        super().__init__(
            name="Throw Stones",
            description="Ein Satz glatter Flusssteine",
            price=0,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.Wurfwaffen,
            tp=1 * Dice(4),
            at_bonus=1
        )